#!/usr/bin/env python3
"""
BITO ERP Documentation Auto-Translator
Uses Google Gemini API (FREE)
Translates one language at a time - run Russian first, then English.
Commits every 10 files so progress is never lost.
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


def git_save(message):
    try:
        subprocess.run(["git", "add", "ru/", "en/"], check=False)
        result = subprocess.run(["git", "diff", "--staged", "--quiet"], capture_output=True)
        if result.returncode != 0:
            subprocess.run(["git", "commit", "-m", message], check=False)
            subprocess.run(["git", "push"], check=False)
            print(f"  >>> Saved to GitHub!", flush=True)
        else:
            print(f"  >>> Nothing new to save.", flush=True)
    except Exception as e:
        print(f"  >>> Git error: {e}", flush=True)


def get_api_key():
    key = os.environ.get("GEMINI_API_KEY")
    if not key:
        print("ERROR: GEMINI_API_KEY not set", flush=True)
        sys.exit(1)
    return key


def clean(text):
    text = text.strip()
    for fence in ["```markdown", "```"]:
        if text.startswith(fence):
            text = text[len(fence):].strip()
            if text.endswith("```"):
                text = text[:-3].strip()
            break
    return text


def translate(api_key, content, lang_code):
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
                return clean(data["candidates"][0]["content"]["parts"][0]["text"])
            elif resp.status_code == 429:
                print(f"  Rate limit, waiting 20s...", flush=True)
                time.sleep(20)
            else:
                print(f"  Error {resp.status_code}", flush=True)
                return content
        except Exception as e:
            print(f"  Error: {e}", flush=True)
            time.sleep(5)
    return content


def should_skip(p):
    return p.suffix.lower() in SKIP_EXTENSIONS or p.name.startswith(".")

def should_copy(p):
    return p.name in COPY_ONLY_FILES


def get_files(uz_dir):
    return [
        (f, f.relative_to(uz_dir))
        for f in sorted(uz_dir.rglob("*"))
        if f.is_file() and not should_skip(f)
    ]


def main():
    # Get target language from environment (ru or en)
    lang_code = os.environ.get("TARGET_LANG", "ru").strip().lower()
    if lang_code not in TARGET_LANGUAGES:
        print(f"ERROR: Unknown language '{lang_code}'. Use 'ru' or 'en'", flush=True)
        sys.exit(1)

    uz_dir = Path("uz")
    out_base = Path(".")

    if not uz_dir.exists():
        print("ERROR: 'uz' directory not found", flush=True)
        sys.exit(1)

    # Setup git
    subprocess.run(["git", "config", "--local", "user.email", "bot@bito.uz"], check=False)
    subprocess.run(["git", "config", "--local", "user.name", "BITO Translator Bot"], check=False)

    files = get_files(uz_dir)
    lang_name = TARGET_LANGUAGES[lang_code]

    print(f"BITO Translator — {lang_name} only", flush=True)
    print(f"Found {len(files)} files\n", flush=True)

    api_key = get_api_key()
    print(f"API key OK\n", flush=True)

    ok = skip = fail = since_commit = 0

    for i, (src, rel) in enumerate(files, 1):
        print(f"[{i}/{len(files)}] {rel}", flush=True)

        dst = out_base / lang_code / rel
        dst.parent.mkdir(parents=True, exist_ok=True)

        # Skip if already translated
        if dst.exists() and dst.stat().st_size > 10:
            print(f"  Already done, skipping.", flush=True)
            skip += 1
            continue

        try:
            content = src.read_text(encoding="utf-8")
        except Exception as e:
            print(f"  Read error: {e}", flush=True)
            fail += 1
            continue

        if should_copy(src):
            dst.write_text(content, encoding="utf-8")
            print(f"  Copied.", flush=True)
            ok += 1
            since_commit += 1
        else:
            print(f"  Translating to {lang_name}...", flush=True)
            result = translate(api_key, content, lang_code)
            dst.write_text(result, encoding="utf-8")
            print(f"  Saved!", flush=True)
            ok += 1
            since_commit += 1
            time.sleep(4)

        # Commit every 10 files
        if since_commit >= 10:
            git_save(f"Auto-translate {lang_code}: {i}/{len(files)} files done")
            since_commit = 0

    # Final commit
    git_save(f"Auto-translate {lang_code}: ALL files complete!")
    print(f"\nDone! Translated:{ok} Skipped:{skip} Failed:{fail}", flush=True)


if __name__ == "__main__":
    main()
