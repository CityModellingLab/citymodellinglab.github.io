---
title: Blog
type: landing
sections:
  - block: hero
    content:
      title: Blog
      text: What we're thinking about...
    design:
      background:
        image: 
          filename: 'welcome.jpg'
          filters:
            brightness: '0.5'
        text_color_light: true
        color: '#333'
      spacing:
        padding: ['30px', '0', '30px', '0']


  - block: collection
    content: 
      filters:
        folders:
          - blog
    design:
      view: card
      columns: '2'
---
