#!/usr/bin/env python3
"""
BITO ERP Documentation Auto-Translator
Uses Google Gemini API (FREE)
Commits every 10 files so progress is saved even if cancelled.
"""

import os
import sys
import time
import subprocess
import requests
from pathlib import Path

TARGET_LANGUAGES = {"ru": "Russian", "en": "English"}
GLOSSARY = "BITO, ERP, CRM, HR, GitBook, Telegram, API, URL"
COPY_ONLY_FILES = {".gitbook.yaml", "SUMMARY.md"}
SKIP_EXTENSIONS = {".json", ".yaml", ".yml", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

PROMPT = """Translate this Uzbek ERP documentation markdown to {lang}.
RULES:
- Output ONLY translated markdown, nothing else
- No code fences around output
- Keep all markdown formatting (#, **, *, >, -, tables, links)
- Never translate: {glossary}
- Never translate URLs, code blocks, image paths
- Use standard {lang} business terminology

TEXT:
{content}"""


def git_commit(message="Auto-translate: save progress"):
    """Commit and push any new translated files."""
    try:
        subprocess.run(["git", "add", "ru/", "en/"], check=False)
        result = subprocess.run(
            ["git", "diff", "--staged", "--quiet"],
            capture_output=True
        )
        if result.returncode != 0:  # there are staged changes
            subprocess.run(["git", "commit", "-m", message], check=False)
            subprocess.run(["git", "push"], check=False)
            print("  >>> Progress saved to GitHub!", flush=True)
        else:
            print("  >>> Nothing new to commit.", flush=True)
    except Exception as e:
        print(f"  >>> Commit error: {e}", flush=True)


def get_api_key():
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        print("ERROR: GEMINI_API_KEY not set", flush=True)
        sys.exit(1)
    return key


def clean(text: str) -> str:
    text = text.strip()
    for fence in ["```markdown", "```"]:
        if text.startswith(fence):
            text = text[len(fence):].strip()
            if text.endswith("```"):
                text = text[:-3].strip()
            break
    return text


def translate(api_key: str, content: str, lang_code: str) -> str:
    if len(content.strip()) < 5:
        return content

    lang = TARGET_LANGUAGES[lang_code]
    prompt = PROMPT.format(lang=lang, glossary=GLOSSARY, content=content)

    for attempt in range(2):
        try:
            resp = requests.post(
                f"{GEMINI_URL}?key={api_key}",
                json={
                    "contents": [{"parts": [{"text": prompt}]}],
                    "generationConfig": {"temperature": 0.1, "maxOutputTokens": 8192}
                },
                timeout=60
            )
            if resp.status_code == 200:
                data = resp.json()
                text = data["candidates"][0]["content"]["parts"][0]["text"]
                return clean(text)
            elif resp.status_code == 429:
                print(f"  Rate limit, waiting 20s...", flush=True)
                time.sleep(20)
            else:
                print(f"  Error {resp.status_code}: {resp.text[:100]}", flush=True)
                return content
        except Exception as e:
            print(f"  Exception: {e}", flush=True)
            if attempt == 0:
                time.sleep(5)
            else:
                return content
    return content


def should_skip(p: Path) -> bool:
    return p.suffix.lower() in SKIP_EXTENSIONS or p.name.startswith(".")

def should_copy(p: Path) -> bool:
    return p.name in COPY_ONLY_FILES


def process(api_key, src: Path, dst: Path, lang_code: str) -> str:
    """Returns: 'skipped', 'ok', or 'fail'"""
    dst.parent.mkdir(parents=True, exist_ok=True)

    # Skip if already translated
    if dst.exists() and dst.stat().st_size > 10:
        print(f"  Already done ({lang_code}), skipping.", flush=True)
        return "skipped"

    try:
        content = src.read_text(encoding="utf-8")
    except Exception as e:
        print(f"  Read error: {e}", flush=True)
        return "fail"

    if should_copy(src):
        dst.write_text(content, encoding="utf-8")
        print(f"  Copied: {src.name}", flush=True)
        return "ok"

    print(f"  Translating to {TARGET_LANGUAGES[lang_code]}...", flush=True)
    result = translate(api_key, content, lang_code)
    dst.write_text(result, encoding="utf-8")
    print(f"  Saved: {dst}", flush=True)
    return "ok"


def get_files(uz_dir: Path):
    return [
        (f, f.relative_to(uz_dir))
        for f in sorted(uz_dir.rglob("*"))
        if f.is_file() and not should_skip(f)
    ]


def main():
    uz_dir = Path("uz")
    out_base = Path(".")
    langs = ["ru", "en"]

    if not uz_dir.exists():
        print(f"Directory 'uz' not found", flush=True)
        sys.exit(1)

    # Setup git
    subprocess.run(["git", "config", "--local", "user.email", "bot@bito.uz"], check=False)
    subprocess.run(["git", "config", "--local", "user.name", "BITO Translator Bot"], check=False)

    print(f"BITO Translator started!", flush=True)
    files = get_files(uz_dir)
    print(f"Found {len(files)} files", flush=True)

    api_key = get_api_key()
    print(f"API key loaded OK\n", flush=True)

    ok = fail = skipped = 0
    files_since_commit = 0

    for i, (src, rel) in enumerate(files, 1):
        print(f"[{i}/{len(files)}] {rel}", flush=True)
        newly_translated = False

        for lang in langs:
            dst = out_base / lang / rel
            result = process(api_key, src, dst, lang)
            if result == "ok":
                ok += 1
                newly_translated = True
            elif result == "skipped":
                skipped += 1
            else:
                fail += 1

        if newly_translated:
            files_since_commit += 1

        # Commit every 10 newly translated files
        if files_since_commit >= 10:
            print(f"\n--- Saving progress to GitHub ---", flush=True)
            git_commit(f"Auto-translate: progress {i}/{len(files)} files")
            files_since_commit = 0

        if not should_copy(src):
            time.sleep(4)

    # Final commit
    print(f"\n--- Final save to GitHub ---", flush=True)
    git_commit("Auto-translate: completed all files")

    print(f"\nDone! Translated:{ok} Skipped:{skipped} Failed:{fail}", flush=True)


if __name__ == "__main__":
    main()
