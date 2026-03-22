# Miguel Anxo Bastos — Sitio Web

[![Build & Deploy](https://github.com/vaijira/miguelanxobastos/actions/workflows/deploy.yaml/badge.svg)](https://github.com/vaijira/miguelanxobastos/actions/workflows/deploy.yaml)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)

Sitio web oficial de **Miguel Anxo Bastos**, economista, filósofo y profesor universitario español. El repositorio contiene tanto la página de inicio como los libros digitales publicados bajo su autoría.

## 📚 Contenido

- **Página principal** — Presentación biográfica y acceso a las obras.
- **Conferencias — Volumen I** — Transcripción y edición de conferencias seleccionadas, compiladas en formato libro mediante [Quarto](https://quarto.org/).

## 🏗️ Estructura del repositorio

```text
├── site/                   # Landing page (HTML + CSS estáticos)
│   ├── index.html
│   └── style.css
├── books/
│   └── es/
│       └── conferencias_miguel_anxo_bastos_vol_i/
│           ├── quarto/     # Fuente del libro (Quarto Markdown)
└── .github/workflows/
    └── deploy.yaml         # CI/CD → Cloudflare Pages
```

## 🚀 Desarrollo local

### Landing page

```bash
python3 -m http.server 8080 --directory site
# Visita http://localhost:8080
```

### Libro (Quarto)

Requiere [Quarto CLI ≥ 1.4](https://quarto.org/docs/get-started/). No es necesario instalar R.

```bash
cd books/es/conferencias_miguel_anxo_bastos_vol_i/quarto
quarto render
# Previsualización en vivo:
quarto preview
```

El output se genera en `_book/`.

## 🌐 Despliegue

El workflow de GitHub Actions compila el libro y despliega automáticamente a **Cloudflare Pages** en cada push a `main`:

1. Configura Quarto CLI.
2. Renderiza el libro con `quarto render`.
3. Despliega `site/` + `_book/` a Cloudflare Pages.

## 📄 Licencia

Este proyecto se distribuye bajo la licencia [GNU GPL v3](LICENSE).
