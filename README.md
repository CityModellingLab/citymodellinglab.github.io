This website is built with Hugo, local templates, Quarto for computational blog posts, and GitHub Pages for deployment.

Small text edits can be made directly in GitHub or a Codespace. For larger changes, use the local setup below.

## 1. Local Setup

### Windows

Install Scoop:

```pwsh
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
iwr -useb get.scoop.sh | iex
```

Install the site tools:

```pwsh
scoop bucket add extras
scoop install git hugo-extended nodejs python quarto
python -m pip install -r requirements-quarto.txt
```

### macOS

Install Homebrew:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

Install the site tools:

```bash
brew update
brew install git hugo node python quarto
python -m pip install -r requirements-quarto.txt
```

Clone and enter the repository:

```bash
git clone https://github.com/shaunhoang/cml-site.git
cd cml-site
```

Preview the Hugo site:

```bash
hugo server
```

Open `http://localhost:1313/`.

## 2. Blog Posts

Blog posts are Hugo page bundles. Each post lives in its own folder:

```text
content/blog/my-post/
  index.md
  featured.jpg
```

Use one of these source formats:

- Plain post: write `content/blog/my-post/index.md`.
- Quarto post: write `content/blog/my-post/index.qmd`, then render it to `index.md`.
- Jupyter notebook post: write `content/blog/my-post/index.ipynb`, then render it to `index.md`.

Hugo publishes `index.md`. It does not execute code by itself. Quarto executes `.qmd` and `.ipynb` posts and generates the Hugo-friendly `index.md`.

### Required Front Matter

Put this at the top of `index.md` or `index.qmd`. For `.ipynb`, put it in the first raw cell.

```yaml
---
title: New Post
date: 2026-05-02
authors:
- Shaun Hoang
- Thomas Murat
summary: The summary shown in preview cards
draft: false
featured: true
tags:
- Mobility Patterns
- Machine Learning
projects: []
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---
```

Notes:

- `authors` should match names under `content/authors/` so author links and profile backlinks work.
- `draft: true` keeps a post out of production pages and member profile post lists.
- `projects` should contain project folder names from `content/project/`, for example `['ai4ci']`.
- Add a featured image named `featured.jpg` in the post folder.

### Rendering Posts

Render one executable post:

```bash
quarto render content/blog/my-post/index.qmd
```

Render all executable posts:


```bash
quarto render
```

Note that only `content/blog/**/index.qmd` and `content/blog/**/index.ipynb` are rendered by the site-wide `quarto render` command.

### Code Blocks And Outputs

By default, Quarto code is shown as folded code blocks with a `Show code` toggle. Show/hide code for one cell with either 

```yaml
# SHOW
#| echo: true 
# HIDE
#| echo: false
```

## 3. Members And Projects

Members live under `content/authors/`. Projects live under `content/project/`.

To add a member:

1. Copy an existing folder under `content/authors/`.
2. Rename the folder to the person’s display name, for example `content/authors/Sherlock Holmes/`.
3. Edit `_index.md`.
4. Add or replace `avatar.jpg`.

Useful member fields include:

```yaml
title: Sherlock Holmes
role: Research Fellow
user_groups:
- Team
bio: Short biography for cards and author blurbs.
interests:
- Urban modelling
education:
  courses:
  - course: PhD in Cities
    institution: UCL
social:
- icon: envelope
  link: mailto:name@example.com
author_aliases:
- S. Holmes
# Use `author_aliases` when publications or posts use a different name from the member page.
```



To add a project:

1. Copy an existing folder under `content/project/`.
2. Rename it with a URL-friendly folder name, for example `content/project/space-syntax-urban-morph/`.
3. Edit `index.md`.
4. Add or replace `featured.jpg`.

Posts and publications can link to projects by listing the project folder name in `projects` in the YAML frontmatter.

## 4. Publications

`publications.bib` is the source file for the Publications section.

To add or update publications:

1. Edit `publications.bib` using standard BibTeX entries.
2. Make sure CML author names match folders under `content/authors/`, or add `author_aliases` to the relevant member page.
3. Commit and push `publications.bib`.

GitHub Actions converts and commits each BibTeX entry into a Hugo page bundle under `content/publication/`, and redeploys the page.

The importer reads common fields

```text
title, author, year, date, journal, booktitle, publisher, doi, abstract, keywords
```

To run the importer locally:

```bash
python scripts/import_publications.py publications.bib content/publication/
hugo server
```

## 5. Publishing Changes

Before pushing, it is recommended to run this to clean-up Hugo elements:

```bash
hugo --minify --renderToMemory
```

Then commit and push to `main`, GitHub Actions builds and deploys the site.

```bash
git status
git add .
git commit -m "Commit message"
git push
```