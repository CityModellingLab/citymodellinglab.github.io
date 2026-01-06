---
### Required
title: "London's permanent accommodation crisis"
date: 2025-05-21
authors: 
- Beatrice Taylor
summary: "At the root of the temporary accommodation crisis is a lack of council housing, but what are councils doing to address it?"
draft: false
featured: true

### Optional
tags:
- Council housing
- London

# Projects linkage
projects: []

# Collaterals
url_code: ''
url_pdf: ''
url_slides: ''
url_video: ''
---

<iframe id="quarto-report" src="/blog/small-council-housing/index_prerendered.html" width="100%" style="border:none; width: 100%; display: block;" scrolling="no"></iframe>

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
