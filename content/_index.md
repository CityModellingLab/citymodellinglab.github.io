---
# Leave the homepage title empty to use the site title
title:
type: landing

sections:
  - block: hero
    content:
      title: |
        Welcome to the City Modelling Lab
      text: |
        <br>
        We take some of the most pressing and complex challenges facing cities such as social inequality and climate change and develop methods, data and tools to enable decision makers to tackle them

    design:
      background:
        image: 
          filename: welcome.jpg
          filters:
            brightness: 0.5
          parallax: true
          position: center
          size: 
          text_color_light: true
        text_color_light: true
        color: '#e61e28'
        
  - block: markdown
    content:
      text: |
        <div style="display:flex; gap:80px; justify-content:center; align-items:center; flex-wrap:nowrap; padding: 0px 0;">
          <a href="https://www.arup.com/services/city-modelling-lab/">
            <img src="home/arup-logo.png" alt="Arup" style="height: 80px; max-width: 100%;">
          </a>
          <a href="https://www.ucl.ac.uk/bartlett/casa">
            <img src="home/casa-logo.png" alt="UCL" style="height: 130px; max-width: 100%;">
          </a>
          <a href="https://www.geo.uzh.ch/">
            <img src="home/uzh-logo.png" alt="UZH" style="height: 80px; max-width: 100%;">
          </a>
        </div>
    design:
      background:
        color: '#fff'
      spacing:
        padding: ['100px', '0', '100px', '0']

  - block: slider
    content:
      slides:
      - title: AI for Collective Intelligence - Smart Cities
        content: Artificial intelligence for smarter city planning 
        align: left
        background:
          image:
            filename: ai4ci-welcome.png
            filters:
              brightness: 0.1
          position: center
          color: '#555'
        link:
          text: Learn More
          url: project/ai4ci
      - title: National Trip End Model Synthetic Population
        content: Building a synthetic population for the UK Department for Transport
        align: left
        background:
          image:
            filename: ntem-welcome.png
            filters:
              brightness: 0.1
          position: center
          color: '#333'
        link:
          text: Learn More
          url: project/ntem
      - title: TRACK-UK
        content: Synthesised Census and Small Area Statistics for Transport and Energy
        align: left
        background:
          image:
            filename: track-uk-welcome.png
            filters:
              brightness: 0.1
          position: center
          color: '#333'
        link:
          text: Learn More
          url: project/track-uk
      - title: GeoMobility
        content: Geodemographics for Equitable Mobility Futures
        align: left
        background:
          image:
            filename: geomobility-welcome.png
            filters:
              brightness: 0.1
          position: center
          color: '#555'
        link:
          text: Learn More
          url: project/geomobility
    design:
      slide_height: ''
      is_fullscreen: true
      # autoplay: true
      loop: true
      interval: 7500
  
  - block: collection
    content:
      title: Latest Posts
      subtitle:
      text:
      count: 3
      filters:
        author: ''
        category: ''
        tag: ''
        folders:
          - blog
      order: desc
    design:
      view: card
      columns: '2'
  
  - block: collection
    content:
      title: Latest Publications
      text: ""
      count: 3
      filters:
        folders:
          - publication
        publication_type: article-journal
      
    design:
      view: citation
      columns: '2'

---
