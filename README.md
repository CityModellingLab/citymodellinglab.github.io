This website is built using Hugo with local templates, deployed with GitHub Pages. You can edit and commit directly on GitHub's codespace for minor text edits, or locally by following these steps.

## 1. Setting up local development

### Windows
- Install Scoop, the Windows package manager

    ```pwsh
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    iwr -useb get.scoop.sh | iex
    # Press `Y` and Enter if asked `Do you want to change the execution policy?`. 
    ```
- Install Hugo and its dependencies

    ```pwsh
    scoop bucket add extras
    scoop install git hugo-extended nodejs python quarto
    python -m pip install -r requirements-quarto.txt
    ```

### Mac
- Install Homebrew, the Mac package manager

    ```pwsh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
    ```
- Install Hugo and its dependencies
    ```pwsh
    brew update && brew upgrade
    brew install git hugo node python quarto
    python -m pip install -r requirements-quarto.txt
    ```

Clone the repository and enter project folder
```bash
# adjust accordingly
git clone https://github.com/shaunhoang/cml-site.git
cd ../cml-site/
```
To start development server (available on `http://localhost:1313/`)
```bash
hugo server
```

If you are editing computational blog posts (`index.qmd` or `index.ipynb`), use Quarto preview instead. This executes the notebook/code cells, writes the generated `index.md`, and runs Hugo for preview:
```bash
quarto preview
```

## 2. Adding a Blog Post

Blog posts are Hugo page bundles. Each post lives in its own folder:

```text
content/blog/my-post/
  index.md
  featured.jpg
```

Hugo only publishes the final `index.md`. It does not execute Python, R, notebooks, or Quarto files. For computational posts, members write `index.qmd` or `index.ipynb`, then render it with Quarto to create/update the final Hugo-friendly `index.md`.

Follow these steps to publish a blog post:

1. Create a post in a new folder in `content/blog/`, e.g.
`content/blog/my-post/index.qmd`
2. **IMPORTANT!** Include YAML front matter at the top of the `.md` and `.qmd` file, or in the first raw cell for `.ipynb`.
    ```yaml
    ---
    ### Required
    title: New Post
    date: 2025-05-02
    authors: # names must match names in content/authors for correct linkage
    - Shaun Hoang
    - Thomas Murat
    summary: The summary that will show up in the preview card
    draft: false
    featured: true

    ### Optional
    tags:
    - Mobility Patterns
    - Machine Learning

    # If the post is linked to any project under content/project/, add the folder's name(s), e.g. ['ai4ci','ntem']. Otherwise, leave blank.
    projects: [] 

    # Add collaterals which will show up as clickable buttons on the post
    url_code: ''
    url_pdf: ''
    url_slides: ''
    url_video: ''
    ---
    ```
3. Add a featured image in the same folder, must be named `featured.jpg`

4. Render the final `index.md`
    - Run from root folder (e.g. `cml-site\>`)
      ```bash
      quarto render content/blog/my-post/index.qmd
      ```
    - Or render all computational posts:
      ```bash
      quarto render
      ```
    - Quarto converts executable posts into Hugo-compatible Markdown at `index.md`. To preview while writing, run:
      ```bash
      quarto preview
      ```
    - To preview a plain Markdown post after editing `index.md`, run:
      ```bash
      hugo server
      ```

The site hides executable source code by default. To show a specific cell, add:

```yaml
#| echo: true
```

For manually generated standalone HTML widgets, place the widget under `static/blog/my-post/` and embed it from `index.md`:

```markdown
{{< html-resource src="/blog/my-post/widget.html" height="560" >}}
```

5. Commit and push to GitHub

    ```bash
    git add .
    git commit -m "Add post"
    git push
    ```

## 3. Adding members and projects

Make a copy of an existing folder under `content/project/` or `content/authors/` and make the desired changes for the new team member or project. Note that the folder's name is important and is how the new project or person can be connected with other resources like blog posts and publications.

For consistency, the naming conventions are:
- Project: single string (e.g., `../project/space-syntax-urban-morph/`)
- People: full name as would appear on publications (e.g., `../authors/Sherlock Holmes/`)

If a person's display name differs from the name used in publications or posts, add aliases in their author front matter:

```yaml
author_aliases:
  - Name on Publication
```

## 4. Updating publications

1. Update `publications.bib` following the BibTex format. Make sure CML authors' names are consistent with their names `content/authors/`.
2. Commit and push this change to GitHub
3. The Publications page and linkages to people will be automatically updated on the website.
