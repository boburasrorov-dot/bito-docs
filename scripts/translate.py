#!/usr/bin/env python3
"""
BITO ERP Documentation Auto-Translator
Uses Google Gemini API (FREE) to translate Uzbek docs to Russian and English.
"""

import os
import sys
import time
import argparse
import urllib.request
import urllib.error
import json
from pathlib import Path

# ─── Configuration ────────────────────────────────────────────────────────────

TARGET_LANGUAGES = {
    "ru": "Russian",
    "en": "English"
}

GLOSSARY = "BITO, ERP, CRM, HR, GitBook, Telegram, API, URL"
COPY_ONLY_FILES = {".gitbook.yaml", "SUMMARY.md"}
SKIP_EXTENSIONS = {".json", ".yaml", ".yml", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}

GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

PROMPT_TEMPLATE = """You are a professional technical translator for ERP software documentation.
Translate the following Uzbek markdown text to {target_language}.

STRICT RULES:
1. Output ONLY the translated markdown. No explanations, no notes, nothing else.
2. Do NOT wrap output in code fences (no ```markdown or ``` at start/end).
3. Keep ALL markdown formatting: #, ##, **, *, >, -, |, [], (), etc.
4. Never translate these terms, keep exactly as-is: {glossary}
5. Never translate content inside code blocks or inline code
6. Never translate URLs, image paths, or file paths
7. Keep all blank lines exactly as in the original
8. Use standard {target_language} business/accounting terminology

TEXT TO TRANSLATE:
{content}"""

# ─── Gemini API ────────────────────────────────────────────────────────────────

def get_api_key():
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        print("ERROR: GEMINI_API_KEY not set")
        sys.exit(1)
    return key


def clean_translation(text: str) -> str:
    text = text.strip()
    if text.startswith("```markdown"):
        text = text[len("```markdown"):].strip()
        if text.endswith("```"):
            text = text[:-3].strip()
    elif text.startswith("```"):
        text = text[3:].strip()
        if text.endswith("```"):
            text = text[:-3].strip()
    return text


def translate_content(api_key: str, content: str, target_lang_code: str, retries=3) -> str:
    if len(content.strip()) < 5:
        return content

    target_language = TARGET_LANGUAGES[target_lang_code]
    prompt = PROMPT_TEMPLATE.format(
        target_language=target_language,
        glossary=GLOSSARY,
        content=content
    )

    payload = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"temperature": 0.1, "maxOutputTokens": 8192}
    }).encode("utf-8")

    url = f"{GEMINI_URL}?key={api_key}"

    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                url,
                data=payload,
                headers={"Content-Type": "application/json"},
                method="POST"
            )
            with urllib.request.urlopen(req, timeout=60) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                translated = data["candidates"][0]["content"]["parts"][0]["text"]
                return clean_translation(translated)

        except urllib.error.HTTPError as e:
            body = e.read().decode()
            if e.code == 429:
                wait = 30 * (attempt + 1)
                print(f"  Rate limit, waiting {wait}s...")
                time.sleep(wait)
            else:
                print(f"  HTTP error {e.code}: {body[:200]}")
                if attempt < retries - 1:
                    time.sleep(10)
                else:
                    return content

        except Exception as e:
            print(f"  Error attempt {attempt+1}: {e}")
            if attempt < retries - 1:
                time.sleep(10)
            else:
                return content

    return content


def should_skip(file_path: Path) -> bool:
    if file_path.suffix.lower() in SKIP_EXTENSIONS:
        return True
    if file_path.name.startswith("."):
        return True
    return False


def should_copy_only(file_path: Path) -> bool:
    return file_path.name in COPY_ONLY_FILES


def process_file(api_key: str, source_file: Path, output_file: Path, lang_code: str) -> bool:
    output_file.parent.mkdir(parents=True, exist_ok=True)

    try:
        content = source_file.read_text(encoding="utf-8")
    except Exception as e:
        print(f"  Cannot read: {e}")
        return False

    if should_copy_only(source_file):
        try:
            output_file.write_text(content, encoding="utf-8")
            print(f"  Copied: {output_file.name}")
            return True
        except Exception as e:
            print(f"  Cannot write: {e}")
            return False

    print(f"  Translating to {TARGET_LANGUAGES[lang_code]}...")
    translated = translate_content(api_key, content, lang_code)

    try:
        output_file.write_text(translated, encoding="utf-8")
        print(f"  Saved: {output_file}")
        return True
    except Exception as e:
        print(f"  Cannot write: {e}")
        return False


def get_files_to_process(uz_dir: Path, changed_files_str: str = None):
    if changed_files_str and changed_files_str.strip():
        files = []
        for line in changed_files_str.strip().split("\n"):
            f = line.strip()
            if not f or not f.endswith(".md"):
                continue
            p = Path(f)
            if p.exists() and not should_skip(p):
                try:
                    rel = p.relative_to(uz_dir)
                    files.append((p, rel))
                except ValueError:
                    files.append((p, Path(p.name)))
        return files
    else:
        files = []
        for f in sorted(uz_dir.rglob("*")):
            if f.is_file() and not should_skip(f):
                rel = f.relative_to(uz_dir)
                files.append((f, rel))
        return files


def main():
    parser = argparse.ArgumentParser(description="BITO ERP Documentation Translator (Gemini)")
    parser.add_argument("--uz-dir", default="uz", help="Source Uzbek docs directory")
    parser.add_argument("--out-dir", default=".", help="Output base directory")
    parser.add_argument("--changed-files", default=None, help="Newline-separated changed files")
    parser.add_argument("--languages", default="ru,en", help="Target language codes")
    parser.add_argument("--dry-run", action="store_true", help="Preview without translating")
    args = parser.parse_args()

    uz_dir = Path(args.uz_dir)
    out_base = Path(args.out_dir)
    target_langs = [l.strip() for l in args.languages.split(",") if l.strip() in TARGET_LANGUAGES]

    if not uz_dir.exists():
        print(f"Source directory '{uz_dir}' not found")
        sys.exit(1)

    print(f"\nBITO ERP Translator (powered by Google Gemini - FREE)")
    print(f"Source : {uz_dir.resolve()}")
    print(f"Targets: {', '.join(TARGET_LANGUAGES[l] for l in target_langs)}")
    print()

    files = get_files_to_process(uz_dir, args.changed_files)

    if not files:
        print("No files to process.")
        return

    print(f"Files to process: {len(files)}")
    for src, rel in files:
        action = "copy" if should_copy_only(src) else "translate"
        print(f"  [{action}] {rel}")

    if args.dry_run:
        print("\nDry run complete.")
        return

    api_key = get_api_key()
    total_ok = 0
    total_fail = 0

    for i, (source_file, relative_path) in enumerate(files, 1):
        print(f"\n[{i}/{len(files)}] {relative_path}")

        for lang_code in target_langs:
            output_file = out_base / lang_code / relative_path
            ok = process_file(api_key, source_file, output_file, lang_code)
            if ok:
                total_ok += 1
            else:
                total_fail += 1

        if not should_copy_only(source_file):
            time.sleep(2)  # Gemini free tier: be gentle

    print(f"\nDone! Success: {total_ok}  Failed: {total_fail}\n")


if __name__ == "__main__":
    main()
