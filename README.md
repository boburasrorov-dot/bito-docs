# 🌐 BITO ERP — Auto Documentation Translator

Automatically translates your Uzbek GitBook docs into **Russian** and **English** every time you make a change. Powered by Claude AI.

---

## How It Works

```
You edit a page in GitBook (Uzbek)
        ↓
GitBook saves to GitHub automatically  
        ↓
GitHub detects the change in uz/ folder
        ↓
Claude AI translates only changed pages
        ↓
Russian (ru/) and English (en/) update automatically
        ↓
GitBook shows updated translations to users
```

---

## Setup Guide (One Time Only)

### Step 1 — Create a GitHub Account and Repository

1. Go to github.com and sign up (free)
2. Click "New repository"
3. Name it: bito-docs
4. Set to Private
5. Click "Create repository"

---

### Step 2 — Upload These Files to GitHub

1. On your new repository page, click "uploading an existing file"
2. Drag and drop ALL files from this ZIP (keep the folder structure)
3. Click "Commit changes"

Your repository should look like this:
```
bito-docs/
├── .github/
│   └── workflows/
│       └── translate.yml
├── scripts/
│   └── translate.py
├── uz/               <- YOUR UZBEK DOCS GO HERE
├── ru/               <- Auto-generated Russian
├── en/               <- Auto-generated English
├── .gitbook.yaml
├── requirements.txt
└── README.md
```

---

### Step 3 — Add Your Claude API Key to GitHub

1. Go to console.anthropic.com
2. Click "API Keys" then "Create Key"
3. Copy the key (starts with sk-ant-...)
4. Go to your GitHub repository
5. Click Settings -> Secrets and variables -> Actions
6. Click "New repository secret"
7. Name: ANTHROPIC_API_KEY
8. Value: paste your API key
9. Click "Add secret"

---

### Step 4 — Connect GitBook to GitHub (Git Sync)

IN GITBOOK (Uzbek space):
1. Open your BITO docs space
2. Click the three dots next to your space name -> "Synchronize with Git"
3. Choose GitHub
4. Authorize GitBook to access your GitHub account
5. Select your bito-docs repository
6. Set branch: main
7. Set monorepo directory: /uz
8. Click Sync

CREATE RUSSIAN SPACE:
1. In GitBook, create a New Space -> name it "BITO Docs RU"
2. Connect it to the same GitHub repo, same branch, directory: /ru

CREATE ENGLISH SPACE:
1. Create another New Space -> name it "BITO Docs EN"
2. Connect it to the same GitHub repo, same branch, directory: /en

---

### Step 5 — Link All Languages on Your Docs Site

1. In GitBook, go to your Docs Site settings
2. Click Structure -> Add variant
3. Add the Russian space, set language to Russian
4. Add the English space, set language to English
5. Publish

Users will now see a language picker in the top-right corner of your docs!

---

## Daily Usage (After Setup)

You only ever edit the Uzbek docs in GitBook. Everything else is automatic.

1. Open GitBook and edit any page in Uzbek
2. GitBook saves to GitHub automatically
3. Translation runs (takes 2-5 minutes)
4. Russian and English pages update automatically

You never touch the ru/ or en/ folders manually.

---

## Translate All Pages at Once (First Time)

After setup, to translate your entire existing documentation:

1. Go to your GitHub repository
2. Click the Actions tab
3. Click "Auto-Translate BITO Docs"
4. Click "Run workflow"
5. Set "Translate ALL pages" to true
6. Click "Run workflow"

This will translate every page in uz/ to both Russian and English.

---

## Costs

Pages translated       | Approximate cost
-----------------------|------------------
50 pages (first run)   | ~$0.50 to $1.00
Daily updates (1-3 pages changed) | ~$0.01 to $0.05/day
Monthly total          | ~$1 to $2/month

---

## Glossary — Terms That Are Never Translated

These terms are kept as-is across all languages:
BITO, ERP, CRM, HR, GitBook, Telegram

To add more protected terms, edit scripts/translate.py and add to the GLOSSARY dictionary.

---

## Troubleshooting

Translation not triggering?
-> Check that you edited a file inside the uz/ folder
-> Check the Actions tab in GitHub for error messages

API key error?
-> Go to GitHub -> Settings -> Secrets -> confirm ANTHROPIC_API_KEY is set

GitBook not showing updates?
-> Check that Git Sync is connected in each GitBook space
-> Try clicking Sync manually in GitBook
# bito-docs
