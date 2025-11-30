# THIS SCRIPT IS USED TO PROCESS THE QUARTO HTML OUTPUTS FOR HUGO INTEGRATION.
# 1. It extracts metadata from the source .qmd or .ipynb files.
# 2. It moves the generated HTML files to the 'static' directory.
# 3. It creates a Hugo-compatible Markdown wrapper with the metadata + an iframe to embed the HTML content.

import os
import shutil
import re
import json
from pathlib import Path

CONTENT_DIR = Path("content")
STATIC_DIR = Path("static")
FORCE_BASE_URL = "/cml-site"  # Only in developpment 
# FORCE_BASE_URL = "" # Use when moved to citymodellinglab.uk

# Template for the Hugo Markdown wrapper
WRAPPER_TEMPLATE = """---
### Required
title: "{title}"
date: {date}
authors: 
{authors}
summary: "{summary}"
draft: {draft}
featured: {featured}

### Optional
tags:
{tags}

# Projects linkage
projects: {projects}

# Collaterals
url_code: '{url_code}'
url_pdf: '{url_pdf}'
url_slides: '{url_slides}'
url_video: '{url_video}'
---

<iframe id="quarto-report" src="{iframe_src}" width="100%" style="border:none; width: 100%; display: block;" scrolling="no"></iframe>

<script>
  (function() {{
    const iframe = document.getElementById('quarto-report');
    if (iframe) {{
      iframe.onload = function() {{
        // Initial Resize
        const body = iframe.contentWindow.document.body;
        const html = iframe.contentWindow.document.documentElement;
        
        const height = Math.max(
            body.scrollHeight, body.offsetHeight, 
            html.clientHeight, html.scrollHeight, html.offsetHeight
        );
        iframe.style.height = height + 'px';

        // Continuous Resize (for interactive elements)
        const resizeObserver = new ResizeObserver(() => {{
           iframe.style.height = iframe.contentWindow.document.body.scrollHeight + 'px';
        }});
        resizeObserver.observe(iframe.contentWindow.document.body);
      }};
    }}
  }})();
</script>
"""

def get_source_content(file_path: Path) -> str:
    """Retrieves raw text content for YAML extraction."""
    try:
        if file_path.suffix == ".ipynb":
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            if "cells" in data and len(data["cells"]) > 0:
                source = data["cells"][0].get("source", [])
                return "".join(source) if isinstance(source, list) else source
        else:
            return file_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""

def parse_front_matter(file_path: Path) -> dict:
    """Extracts YAML front matter handling both inline and block lists."""
    meta = {
        "title": "Untitled", "date": "2025-01-01", "authors": [], 
        "summary": "", "tags": [], "projects": [], "draft": "false", 
        "featured": "true", "url_code": "", "url_pdf": "", 
        "url_slides": "", "url_video": ""
    }
    
    content = get_source_content(file_path)
    match = re.search(r"^---\s*\n(.*?)\n---", content.strip(), re.DOTALL)
    
    if match:
        current_list_key = None
        yaml_lines = match.group(1).split('\n')
        
        for line in yaml_lines:
            line = line.strip()
            if not line or line.startswith('#'): continue

            # 1. Handle List Items (e.g. "- Item")
            if line.startswith('- '):
                val = line[2:].split('#')[0].strip().strip('"\'')
                if current_list_key and isinstance(meta.get(current_list_key), list):
                    meta[current_list_key].append(val)
                continue

            # 2. Handle Key-Value pairs
            if ':' in line:
                key_part, val_part = line.split(':', 1)
                key = key_part.strip()
                val = val_part.split('#')[0].strip().strip('"\'')
                
                # Identify if this is a block list start (empty value)
                if not val:
                    if key in ["authors", "author", "tags", "projects"]:
                        # Map singular 'author' to plural 'authors' list
                        current_list_key = "authors" if key == "author" else key
                    else:
                        current_list_key = None
                    continue

                # It's a standard key-value
                current_list_key = None 
                
                if key in meta and isinstance(meta[key], str):
                    meta[key] = val
                elif key == "author":
                    meta["authors"].append(val)
                elif key in ["tags", "projects"]:
                    # Handle inline list syntax: [a, b]
                    clean_val = [x.strip().strip('"\'') for x in val.strip("[]").split(',') if x.strip()]
                    meta[key] = clean_val
                elif key in ["abstract", "description"]:
                    meta["summary"] = val

    return meta

def clean_html_content(html_path: Path):
    """Removes Quarto's default title block header from the HTML file."""
    try:
        content = html_path.read_text(encoding="utf-8")
        # Remove the <header id="title-block-header"> section
        cleaned = re.sub(r'<header id="title-block-header".*?</header>', '', content, flags=re.DOTALL)
        html_path.write_text(cleaned, encoding="utf-8")
    except Exception as e:
        print(f"Warning: Could not clean HTML content: {e}")

def create_hugo_wrapper(md_path: Path, iframe_src: str, meta: dict):
    """Creates the index.md file using the global template."""
    
    def fmt_list(items): 
        return "\n".join([f"- {i}" for i in items]) if items else ""

    # Prepare context for the template
    context = {
        **meta,
        "authors": fmt_list(meta['authors']),
        "tags": fmt_list(meta['tags']),
        "projects": json.dumps(meta['projects']) if meta['projects'] else "[]",
        "iframe_src": iframe_src
    }

    content = WRAPPER_TEMPLATE.format(**context)
    
    md_path.write_text(content, encoding="utf-8")
    print(f"Generated Wrapper: {md_path}")

def process_file(html_file_str: str):
    html_path = Path(html_file_str).resolve()
    if not html_path.exists(): return

    # 1. Validate Path (Must be inside CONTENT_DIR)
    try:
        # Determine path relative to 'content' (e.g., blog/my-post)
        rel_path = html_path.parent.relative_to(Path(CONTENT_DIR).resolve())
    except ValueError:
        return # File is not in the content directory

    # 2. Identify Source File (.qmd or .ipynb)
    source_file = next(
        (html_path.with_suffix(ext) for ext in [".qmd", ".ipynb"] if html_path.with_suffix(ext).exists()), 
        None
    )
    
    if not source_file:
        print(f"Skipping {html_path.name}: No source .qmd or .ipynb found.")
        return

    # 3. Clean HTML
    clean_html_content(html_path)

    # 4. Move HTML to static
    # Target: static/blog/my-post/index_prerendered.html
    target_dir = STATIC_DIR / rel_path
    target_file = target_dir / "index_prerendered.html"
    
    target_dir.mkdir(parents=True, exist_ok=True)
    shutil.move(str(html_path), str(target_file))
    print(f"Moved HTML to: {target_file}")

    # 5. Generate Wrapper
    # Iframe src: /blog/my-post/index_prerendered.html
    iframe_src = f"{FORCE_BASE_URL}/{rel_path.as_posix()}/index_prerendered.html"
    create_hugo_wrapper(html_path.with_name("index.md"), iframe_src, parse_front_matter(source_file))

if __name__ == "__main__":
    # Process files passed by Quarto
    files = os.environ.get("QUARTO_PROJECT_OUTPUT_FILES", "").split("\n")
    for f in files:
        if f.endswith(".html"): 
            process_file(f)