---
### Required
title: "A post rendered from a Jupyter notebook (.ipynb)"
date: 2025-05-02
authors: 
- Beatrice Taylor
- Claude Lynch
summary: "The summary that will show up in the preview card"
draft: false
featured: true

### Optional
tags:
- Housing
- Urban Planning

# Projects linkage
projects: ["ai4ci"]

# Collaterals
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

<iframe id="quarto-report" src="/cml-site/blog/post3-jupyter/index_prerendered.html" width="100%" style="border:none; width: 100%; display: block;" scrolling="no"></iframe>

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
