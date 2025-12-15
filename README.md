This website is built using Hugo and Hugo Blox, deployed with GitHub Pages. You can edit and commit directly on GitHub's codespace (only minor text edits), or locally (recommended for stability) by following these steps.

## 1. Set up for local development

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
    scoop install git go hugo-extended nodejs quarto
    ```

### Mac
- Install Homebrew, the Mac package manager

    ```pwsh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
    ```
- Install Hugo and its dependencies
    ```pwsh
    brew update && brew upgrade
    brew install git golang hugo node quarto
    ```

Clone the repository and enter project folder
```bash
git clone https://github.com/shaunhoang/cml-site.git
cd ../cml-site/ # adjust accordingly
```
Inititalise project
```bash
hugo mod tidy
```
To start development server (available on `http://localhost:1313/`)
```bash
hugo server
```

## 2. Adding a Blog Post 

Blog posts are in markdown format. For blogposts with executable codes, render `index.md` documents from `.md`, `.qmd` or `.ipynb` locally before pushing the changes to GitHub repo for build. Here's how:

1. Create a post in a new folder in `content/blog/`, e.g.
`content/blog/my-post/my-post.ipynb`
2. **IMPORTANT!** Include YAML front matter at the top of the `.md` and `.qmd` file (or first cell for `.ipynb` in `raw` format). 
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

4. Execute codes and render locally
    - Run from root folder (e.g. `C:\...\cml-site>`)
      ```bash
      quarto render content/blog/my-post/my-post.qmd  
      # or quarto render content/blog/my-post/my-post.md
      # or quarto render content/blog/my-post/my-post.ipynb
      ```
    - Quarto has been configured to convert them into a Hugo-compatible markdown file `index.md`. Verify it has been generated inside the folder. (You should also see a new output created under `static/blog/...`)

5. Commit and push to GitHub

    ```bash
    git add .
    git commit -m "Add post"
    git push
    ```

## 3. Adding members and projects

Make a copy of an existing folder under `content/project/` or `content/authors/` and make an desired changes for the new team member / project. Note that the folder's name is important and is how the new project or person can be connected with other resources like blog posts and publications. 

For consistency, the naming conventions are:
- Project: single string (e.g., `../project/space-syntax-urban-morph/`)
- People: full name as would appear on publications (e.g., `../authors/Sherlock Holmes/`)

## 4. Updating publications

1. Under `data/`, update `publications.bib` following the BibTex format. Make sure CML authors' names are consistent with their names `content/authors/`.
2. Commit and push this change to GitHub
3. The Publications page and linkages to people will be automatically updated on the website.
