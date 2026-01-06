---
### Required
title: "Some other post rendered from .qmd"
date: 2025-07-02
authors: 

summary: "The summary that will show up in the preview card"
draft: true
featured: true

### Optional
tags:
- Council housing
- London

# Projects linkage
projects: ["ntem"]

# Collaterals
url_code: ''
url_pdf: ''
url_slides: ''
url_video: 'https://www.youtube.com/watch?v=-2xD3C03HvI'
---

<iframe id="quarto-report" src="/blog/post2-qmd/index_prerendered.html" width="100%" style="border:none; width: 100%; display: block;" scrolling="no"></iframe>

<script>
  (function() {
    const iframe = document.getElementById('quarto-report');
    if (iframe) {
      iframe.onload = function() {
        // Initial Resize
        const body = iframe.contentWindow.document.body;
        const html = iframe.contentWindow.document.documentElement;
        
        const height = Math.max(
            body.scrollHeight, body.offsetHeight, 
            html.clientHeight, html.scrollHeight, html.offsetHeight
        );
        iframe.style.height = height + 'px';

        // Continuous Resize (for interactive elements)
        const resizeObserver = new ResizeObserver(() => {
           iframe.style.height = iframe.contentWindow.document.body.scrollHeight + 'px';
        });
        resizeObserver.observe(iframe.contentWindow.document.body);
      };
    }
  })();
</script>
