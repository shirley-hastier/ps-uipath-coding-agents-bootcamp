# Professional Services UiPath for Coding Agents Builder Bootcamp — Site

Hands-on bootcamp handbook teaching Professional Services how to build UiPath
agents and Maestro orchestrations with coding agents (Claude Code) and the
`uip` CLI.

Built on the same MkDocs framework as the
[UiPath Coding Agents Workshop](https://uipath-practice.github.io/CodingAgentsCourse/)
(MkDocs Material + a `mkdocs-macros` environment-variable module + a small
two-column layout hook).

## Access the "Lab Guide" using the link below

[Professional Services UiPath for Coding Agents Builder Bootcamp](https://shirley-hastier.github.io/ps-uipath-coding-agents-bootcamp/)

> **This repo's `docs/` is generated — do not hand-edit it.** Content is
> authored in a private companion repo
> (`ps-uipath-coding-agents-bootcamp-coach`) and published here with the
> Coach View sections stripped. Edits made directly here will be
> overwritten by the next publish.

## How it works

```
docs/*.md  ->  MkDocs builds HTML  ->  GitHub Actions  ->  gh-pages  ->  GitHub Pages
```

| Path | Purpose |
|------|---------|
| `docs/` | Published page content — one `.md` per page |
| `mkdocs.yml` | Site config + nav |
| `main.py` | Environment variables (staging vs prod) for the training callout |
| `hooks/split_cols.py` | Two-column layout shorthand (`[[[ ... \|30\| ... ]]]`) |
| `.github/workflows/deploy.yml` | Auto-deploy to GitHub Pages on push to `main` |

## First-time setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Preview locally
BOOTCAMP_ENV=staging mkdocs serve
# open http://127.0.0.1:8000

# 3. Release-equivalent build check
BOOTCAMP_ENV=prod mkdocs build
```

## Environments

| `BOOTCAMP_ENV` | Account / URL | Tenant | When |
|----------------|---------------|--------|------|
| `staging` | staging.uipath.com/partnersuccess | Workshops | While authoring |
| `prod` (default) | cloud.uipath.com/tpenlabs | CodingAgentsBootcamp | Live site (CI) |

CI always builds with `prod`. Switch locally with the `BOOTCAMP_ENV` variable.
