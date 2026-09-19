---
title: ''
date: 2022-10-24
type: landing

# Hide the social-media share row and "N min read" badge on every page site-wide.
cascade:
  - params:
      share: false
      reading_time: false

sections:
  - block: resume-biography-3
    id: about
    content:
      username: me
      text: ''
      headings:
        about: ''
        interests: Research Interests
    design:
      background:
        gradient_mesh:
          enable: true
      name:
        size: md
      avatar:
        size: medium
        shape: circle

  - block: markdown
    id: featured
    content:
      title: Featured
      text: |-
        {{< youtube 7S_VqFJep_0 >}}

        Our group's outreach video on the magnetic fields of the planets in our solar system, paired with **[planetMagFields](https://planetmagfields.streamlit.app)** — an interactive web app for exploring planetary magnetic field data, built on the open-source [planetMagFields](/project/software/#planetmagfields) Python package.

        {{< button url="https://planetmagfields.streamlit.app" text="Try the app" icon="rocket-launch" style="primary" size="md" new_tab="true" />}}
    design:
      columns: '1'

  - block: markdown
    id: codes
    content:
      title: Codes I Build
      text: |-
        {{< cards cols="3" >}}
        {{< card url="/project/software/#magic" title="MagIC" subtitle="3D MHD code — used in 170+ papers" icon="bolt" >}}
        {{< card url="/project/software/#kore" title="Kore" subtitle="Spectral MHD eigenvalue solver" icon="code-bracket" >}}
        {{< card url="/project/software/#planetmagfields" title="planetMagFields" subtitle="Visualize planetary magnetic field data" icon="globe-alt" >}}
        {{< /cards >}}
    design:
      columns: '1'

  - block: portfolio
    id: projects
    content:
      title: Projects
      count: 6
      sort_by: Weight
      sort_ascending: true
      filters:
        folders:
          - project
      archive:
        link: /project/
        text: See all projects
    design:
      columns: 3
      fallback_icon: beaker

  - block: collection
    id: publications
    content:
      title: Publications
      count: 4
      filters:
        folders:
          - publication
    design:
      view: citation

  - block: collection
    id: teaching
    content:
      title: Teaching
      filters:
        folders:
          - teaching
    design:
      view: article-grid
      columns: 3
      show_date: false
      show_read_time: false

  - block: contact-info
    id: contact
    content:
      title: Contact
      visit_title: Visit
      connect_title: Connect
      address:
        lines:
          - Olin Hall, 224
          - 3400 N Charles Street
          - Baltimore, MD 21218
          - United States
      email: abarik@jhu.edu
      social:
        - icon: brands/bluesky
          url: https://bsky.app/profile/astrodoc.bsky.social
      map_url: 'https://www.google.com/maps/search/?api=1&query=39.328154,-76.623674'
---
