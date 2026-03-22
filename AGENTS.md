# AGENTS.md — Miguel Anxo Bastos Website

This file describes the repository structure and guidelines for AI coding agents working on this project.

## Repository Overview

Static website for **Miguel Anxo Bastos**, a Spanish economist and professor. It consists of:

- A **landing page** (`site/`) — static HTML + CSS.
- A **Quarto book** (`books/es/conferencias_miguel_anxo_bastos_vol_i/quarto/`) — Quarto Markdown source compiled to HTML.
- A **CI/CD pipeline** (`.github/workflows/deploy.yaml`) — builds the book and deploys both assets to **Cloudflare Pages**.

## Directory Structure

```
site/                        # Landing page (static HTML + CSS)
│   index.html
│   style.css
│   _redirects               # Cloudflare Pages redirect rules
books/
└── es/
    └── conferencias_miguel_anxo_bastos_vol_i/
        ├── quarto/          # Quarto book source (active)
        │   ├── _quarto.yml  # Book config (title, chapters, theme)
        │   ├── index.qmd    # Introduction
        │   ├── 01-*.qmd     # Chapter files (numbered)
        │   ├── references.qmd
        │   ├── book.bib
        │   ├── styles.css
        │   └── _book/       # Build output (git-ignored)
        └── bookdown/        # Legacy R Markdown source (kept for reference)
.github/workflows/
└── deploy.yaml              # Build + deploy to Cloudflare Pages
```

## Local Development

### Landing page

```bash
python3 -m http.server 8080 --directory site
# Visit http://localhost:8080
```

### Quarto book

Requires [**Quarto CLI ≥ 1.4**](https://quarto.org/docs/get-started/). No R installation needed.

Build:

```bash
cd books/es/conferencias_miguel_anxo_bastos_vol_i/quarto
quarto render
```

Output is written to `_book/`. Preview with live-reload:

```bash
quarto preview
```

## CI/CD

The `deploy.yaml` workflow runs on every push to `main`/`master`:

1. Sets up Quarto CLI (bundles its own Pandoc).
2. Renders the book with `quarto render`.
3. Assembles `_site/`: landing page at root, book under `/conferencias_vol_i/`.
4. Deploys `_site/` to Cloudflare Pages (push events only).

Required repository secrets:

| Secret | Description |
|---|---|
| `CLOUDFLARE_API_TOKEN` | Cloudflare API token with Pages deploy permission |
| `CLOUDFLARE_ACCOUNT_ID` | Cloudflare account ID |

## Authoring Guidelines

### Adding or editing book chapters

- Chapter files are named `NN-slug.qmd` (e.g. `03-el-fracaso-de-la-agenda-2030.qmd`) inside `quarto/`.
- The build order is controlled by the `chapters:` list in `_quarto.yml`. Add new chapters there.
- Prose is in **Spanish**. Maintain that language for all book content.
- Citations use the BibTeX file `book.bib` and Chicago full-note style (`chicago-fullnote-bibliography.csl`).
- Use `{.unnumbered}` (not `{-}`) for unnumbered section headings.

### Editing the landing page

- Modify `site/index.html` and `site/style.css` directly.
- The page is purely static: no build step, no framework, no bundler.
- Keep styles in `style.css`; avoid inline styles.

### Redirects

- Cloudflare Pages redirect rules live in `site/_redirects`.

## Agent Rules

- **Do not commit build artifacts**: `_book/`, `_site/`, `.wrangler/` are generated — never add them to git.
- **Do not change the license**: The project is GPL v3. Do not relicense any file.
- **Preserve Spanish**: All user-facing content (book prose, landing page copy) is in Spanish. Do not translate it.
- **Minimal dependencies**: Do not add Quarto extensions without updating both `deploy.yaml` and the local install instructions above.
- **No framework churn**: The landing page is intentionally plain HTML/CSS. Do not introduce JavaScript frameworks, bundlers, or CSS preprocessors.
- **Do not edit `bookdown/`**: That directory is kept as a legacy reference only; all active authoring happens in `quarto/`.
