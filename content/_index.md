---
# Leave the homepage title empty to use the site title
title:
type: landing

sections:
  - block: hero
    content:
      title: |
        Welcome to the CASA / Arup City Modelling Lab
      text: |
        <br>
        Here at the City Modelling Lab we take some of the most pressing and complex challenges facing cities such as social inequality and climate change and develop methods, data and tools to enable decision makers to tackle them.
        <br>

    design:
      background:
        image: 
          filters:
            brightness: '0.5'
        text_color_light: true
        color: '#333'
        
  - block: markdown
    content:
      text: |
        <div style="display:flex; gap:120px; justify-content:center; align-items:center; flex-wrap:wrap;">
          <a href="https://www.ucl.ac.uk/bartlett/casa">
            <img src="/media/ucl-logo.png" alt="UCL" style="height: 60px; max-width: 100%;">
          </a>
          <a href="https://www.arup.com/">
            <img src="/media/arup-logo.png" alt="Arup" style="height: 60px; max-width: 100%;">
          </a>
          <a href="https://www.geo.uzh.ch/">
            <img src="/media/uzh-logo.png" alt="UZH" style="height: 60px; max-width: 100%;">
          </a>
        </div>

  - block: slider
    content:
      slides:
      - title: "Artificial Intelligence for Collective Intelligence (AI4CI) - Smart Cities"
        content: A new research hub to address society’s most pressing challenges we need new kinds of Collective Intelligence
        align: left
        background:
          image:
            filename: welcome.jpg
            filters:
              brightness: 0.6
          position: center
          color: '#555'
        link:
          text: Learn More
          url: ../project/ai4ci
      - title: National Trip End Model Synthetic Population
        content: A synthetic population for the Department for Transport
        align: left
        background:
          image:
            filename: welcome.jpg
            filters:
              brightness: 0.6
          position: center
          color: '#333'
        link:
          text: Learn More
          url: ../project/ntem
    design:
      slide_height: ''
      is_fullscreen: true
      loop: false
      interval: 2000
  
  - block: collection
    content:
      title: Blog
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
        folders:
          - blog
      order: desc
    design:
      view: card
      columns: '2'
  
  # - block: markdown
  #   content:
  #     title:
  #     subtitle: ''
  #     text:
  #   design:
  #     columns: '1'
  #     background:
  #       image: 
  #         filename: coders.jpg
  #         filters:
  #           brightness: 1
  #         parallax: false
  #         position: center
  #         size: cover
  #         text_color_light: true
  #     spacing:
  #       padding: ['20px', '0', '20px', '0']
  #     css_class: fullscreen

  - block: collection
    content:
      title: Latest Publications
      text: ""
      count: 3
      filters:
        folders:
          - publication
        # publication_type: 'article'
    design:
      view: citation
      columns: '1'

---
