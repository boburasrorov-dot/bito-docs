#!/usr/bin/env python3
"""
BITO ERP Documentation Auto-Translator
Uses Google Gemini API (FREE) - Russian and English
"""

import os
import sys
import time
import argparse
import json
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


def process(api_key, src: Path, dst: Path, lang_code: str) -> bool:
    dst.parent.mkdir(parents=True, exist_ok=True)
    try:
        content = src.read_text(encoding="utf-8")
    except Exception as e:
        print(f"  Read error: {e}", flush=True)
        return False

    if should_copy(src):
        dst.write_text(content, encoding="utf-8")
        print(f"  Copied: {src.name}", flush=True)
        return True

    print(f"  Translating to {TARGET_LANGUAGES[lang_code]}...", flush=True)
    result = translate(api_key, content, lang_code)
    dst.write_text(result, encoding="utf-8")
    print(f"  Saved: {dst}", flush=True)
    return True


def get_files(uz_dir: Path, changed_str=None):
    if changed_str and changed_str.strip():
        files = []
        for line in changed_str.strip().split("\n"):
            f = line.strip()
            if f and f.endswith(".md"):
                p = Path(f)
                if p.exists() and not should_skip(p):
                    try:
                        rel = p.relative_to(uz_dir)
                    except ValueError:
                        rel = Path(p.name)
                    files.append((p, rel))
        return files
    return [
        (f, f.relative_to(uz_dir))
        for f in sorted(uz_dir.rglob("*"))
        if f.is_file() and not should_skip(f)
    ]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--uz-dir", default="uz")
    parser.add_argument("--out-dir", default=".")
    parser.add_argument("--changed-files", default=None)
    parser.add_argument("--languages", default="ru,en")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    uz_dir = Path(args.uz_dir)
    out_base = Path(args.out_dir)
    langs = [l.strip() for l in args.languages.split(",") if l.strip() in TARGET_LANGUAGES]

    if not uz_dir.exists():
        print(f"Directory '{uz_dir}' not found", flush=True)
        sys.exit(1)

    print(f"BITO Translator started!", flush=True)
    print(f"Source: {uz_dir} | Targets: {', '.join(langs)}", flush=True)

    files = get_files(uz_dir, args.changed_files)
    if not files:
        print("No files found.", flush=True)
        return

    print(f"Found {len(files)} files", flush=True)

    if args.dry_run:
        for src, rel in files:
            print(f"  {rel}", flush=True)
        return

    api_key = get_api_key()
    print(f"API key loaded OK", flush=True)
    ok = fail = 0

    for i, (src, rel) in enumerate(files, 1):
        print(f"[{i}/{len(files)}] {rel}", flush=True)
        for lang in langs:
            dst = out_base / lang / rel
            if process(api_key, src, dst, lang):
                ok += 1
            else:
                fail += 1
        if not should_copy(src):
            time.sleep(4)

    print(f"Done! OK:{ok} Failed:{fail}", flush=True)


if __name__ == "__main__":
    main()
