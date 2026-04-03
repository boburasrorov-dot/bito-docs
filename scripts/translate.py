#!/usr/bin/env python3
"""
BITO ERP Documentation Auto-Translator
Translates Uzbek GitBook markdown files to Russian and English using Claude AI.
"""

import os
import sys
import json
import time
import argparse
import anthropic
from pathlib import Path

# ─── Configuration ────────────────────────────────────────────────────────────

TARGET_LANGUAGES = {
    "ru": "Russian",
    "en": "English"
}

# Terms that should NEVER be translated (ERP module names, UI buttons, etc.)
GLOSSARY = {
    "BITO": "BITO",
    "ERP": "ERP",
    "CRM": "CRM",
    "HR": "HR",
    "GitBook": "GitBook",
    "Telegram": "Telegram",
}

SYSTEM_PROMPT = """You are a professional technical translator specializing in ERP software documentation.
Your task is to translate Uzbek documentation to {target_language}.

STRICT RULES:
1. Translate ONLY the text content. Never change markdown formatting (**, *, #, >, -, [], (), etc.)
2. Never translate these terms — keep them exactly as-is: {glossary}
3. Never translate code blocks (content inside ``` ```)
4. Never translate URLs, file paths, or image paths
5. Never translate UI element names that appear in the software (keep them as shown in the app)
6. Keep all markdown structure identical — same headings, same bullet points, same tables
7. Output ONLY the translated markdown. No explanations, no preamble, no notes.
8. For technical ERP terms, use the standard {target_language} business/accounting terminology
9. Preserve all empty lines and spacing exactly as in the original"""

# ─── Translation Engine ────────────────────────────────────────────────────────

def get_client():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ ERROR: ANTHROPIC_API_KEY environment variable not set")
        sys.exit(1)
    return anthropic.Anthropic(api_key=api_key)


def translate_content(client, content: str, target_lang_code: str) -> str:
    """Translate markdown content using Claude API."""
    target_language = TARGET_LANGUAGES[target_lang_code]
    glossary_str = ", ".join(GLOSSARY.keys())

    # Skip translation for very short files or empty files
    if len(content.strip()) < 10:
        return content

    try:
        message = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=8096,
            system=SYSTEM_PROMPT.format(
                target_language=target_language,
                glossary=glossary_str
            ),
            messages=[
                {
                    "role": "user",
                    "content": f"Translate this Uzbek documentation to {target_language}:\n\n{content}"
                }
            ]
        )
        translated = message.content[0].text
        return translated

    except anthropic.RateLimitError:
        print("  ⏳ Rate limit hit, waiting 60 seconds...")
        time.sleep(60)
        return translate_content(client, content, target_lang_code)

    except anthropic.APIError as e:
        print(f"  ❌ API error: {e}")
        return content  # Return original on error


def should_skip_file(file_path: Path) -> bool:
    """Skip non-documentation files."""
    skip_names = {"SUMMARY.md", "README.md", ".gitbook.yaml"}
    skip_extensions = {".json", ".yaml", ".yml", ".png", ".jpg", ".gif", ".svg"}

    if file_path.name in skip_names:
        return True
    if file_path.suffix.lower() in skip_extensions:
        return True
    return False


# ─── File Processing ───────────────────────────────────────────────────────────

def translate_file(client, source_file: Path, output_dir: Path, lang_code: str) -> bool:
    """Translate a single markdown file and save to output directory."""
    try:
        content = source_file.read_text(encoding="utf-8")
    except Exception as e:
        print(f"  ❌ Could not read {source_file}: {e}")
        return False

    print(f"  🔄 Translating to {TARGET_LANGUAGES[lang_code]}...")
    translated = translate_content(client, content, lang_code)

    # Create output path mirroring source structure
    output_file = output_dir / source_file.name
    output_file.parent.mkdir(parents=True, exist_ok=True)

    try:
        output_file.write_text(translated, encoding="utf-8")
        print(f"  ✅ Saved: {output_file}")
        return True
    except Exception as e:
        print(f"  ❌ Could not save {output_file}: {e}")
        return False


def get_changed_files(uz_dir: Path, changed_files_str: str = None):
    """Get list of markdown files to translate."""
    if changed_files_str:
        # From GitHub Actions: only translate changed files
        files = []
        for f in changed_files_str.strip().split("\n"):
            f = f.strip()
            if f and f.endswith(".md"):
                full_path = Path(f)
                if full_path.exists():
                    files.append(full_path)
        return files
    else:
        # Translate all files in the uz directory
        return [f for f in uz_dir.rglob("*.md") if not should_skip_file(f)]


# ─── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="BITO ERP Documentation Translator")
    parser.add_argument("--uz-dir", default="uz", help="Source Uzbek docs directory")
    parser.add_argument("--out-dir", default=".", help="Output base directory (ru/ and en/ created here)")
    parser.add_argument("--changed-files", default=None, help="Newline-separated list of changed files (for CI)")
    parser.add_argument("--languages", default="ru,en", help="Comma-separated target language codes")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be translated without doing it")
    args = parser.parse_args()

    uz_dir = Path(args.uz_dir)
    out_base = Path(args.out_dir)
    target_langs = [l.strip() for l in args.languages.split(",") if l.strip() in TARGET_LANGUAGES]

    if not uz_dir.exists():
        print(f"❌ Source directory '{uz_dir}' not found")
        sys.exit(1)

    print(f"\n🚀 BITO ERP Translator")
    print(f"   Source: {uz_dir.resolve()}")
    print(f"   Languages: {', '.join(TARGET_LANGUAGES[l] for l in target_langs)}")
    print()

    # Get files to translate
    files = get_changed_files(uz_dir, args.changed_files)

    if not files:
        print("✅ No markdown files to translate.")
        return

    print(f"📄 Files to translate: {len(files)}")
    for f in files:
        print(f"   - {f}")

    if args.dry_run:
        print("\n🔍 Dry run — no translation performed.")
        return

    # Initialize Claude client
    client = get_client()

    # Translate each file into each language
    total_success = 0
    total_fail = 0

    for file_path in files:
        print(f"\n📄 {file_path.name}")

        for lang_code in target_langs:
            # Mirror directory structure: uz/savdo/page.md → ru/savdo/page.md
            relative = file_path.relative_to(uz_dir) if file_path.is_relative_to(uz_dir) else Path(file_path.name)
            lang_out_dir = out_base / lang_code / relative.parent

            success = translate_file(client, file_path, lang_out_dir, lang_code)
            if success:
                total_success += 1
            else:
                total_fail += 1

        time.sleep(1)  # Small delay between files to be polite to the API

    print(f"\n🎉 Done! {total_success} translations successful, {total_fail} failed.")


if __name__ == "__main__":
    main()
