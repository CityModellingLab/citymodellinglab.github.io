This website is built using Hugo and Hugo Blox. You can edit and commit directly on GitHub's codespace, or edit locally.

**Note:** 

## 1. Set up local development env

### Windows
- Install Scoop, the package manager for Windows
    ```pwsh
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
    iwr -useb get.scoop.sh | iex
    # Press `Y` and enter if asked `Do you want to change the execution policy?`. 
    ```
- Then install Hugo and its dependencies
    ```pwsh
    scoop install git go hugo-extended nodejs
    ```

### Mac
- Install Homebrew, the Mac package manager,
    ```pwsh
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
    ```
- Apply any Homebrew updates:

    ```pwsh
    brew update && brew upgrade
    ```
- Install Hugo and its dependencies
    ```pwsh
    brew install git golang hugo node
    ```
## 2. Start Development server
```pwsh
hugo server
```

## 3. Adding a Blog Post 

Blog posts are in markdown format. If necessary, render `index.md` documents from `.qmd` or `.ipynb` formats **locally before pushing** the changes to GitHub repo for build. 

1. Create a post in a new folder in `content/blog/`. The source file must be named `index` for correct rendering. E.g.
    - Markdown: `content/blog/my-post/index.md`, or
    - Quarto: `content/blog/my-post/index.qmd`, or
    - Jupyter: `content/blog/my-post/index.ipynb`
2. Remember to include YAML front matter at the top of the `.md` and `.qmd` file (or first cell for `.ipynb` in `raw` format).
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
4. Add a featured image in the same folder, to be named `featured.jpg`

5. Follow these steps only to render `.qmd` and `.ipynb` locally. If the file is already `index.md`, skip to #6.
    - Install [Quarto](https://quarto.org/docs/get-started/)
    - To render, run from root folder (i.e., where the `_quarto.yml` file is located)
      ```pwsh
      quarto render content/blog/my-post/index.qmd  
      # or quarto render content/blog/my-post/index.ipynb
      ```
    - Verify `index.md` and `index_files/` were generated, 

6. Commit everything

    ```pwsh
    git add .
    git commit -m "Add post"
    git push
    ```
