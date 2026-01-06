---
### Required
title: "A post rendered from Markdown (.md)"
date: 2025-10-02
authors: 

summary: "The summary that will show up in the preview card"
draft: true
featured: true

### Optional
tags:
- Mobility Patterns
- Machine Learning

# Projects linkage
projects: []

# Collaterals
url_code: 'https://github.com/CityModellingLab/'
url_pdf: ''
url_slides: 'https://adamdennett.github.io/AUM2024/AUM2024Presentation.html'
url_video: 'https://www.youtube.com/watch?v=JrhGCrtiXNw'
---

<iframe id="quarto-report" src="/blog/post1-md/index_prerendered.html" width="100%" style="border:none; width: 100%; display: block;" scrolling="no"></iframe>

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
