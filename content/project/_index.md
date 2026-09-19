---
title: Projects
type: landing

# Hide the author bio box at the bottom of each project's detail page.
cascade:
  - params:
      profile: false

sections:
  - block: portfolio
    id: projects
    content:
      title: Projects
      filters:
        folders:
          - project
      default_button_index: 0
      buttons:
        - name: All
          tag: '*'
        - name: Dynamos
          tag: Dynamos
        - name: Fluid dynamics
          tag: Fluid dynamics
        - name: Magnetosphere
          tag: Magnetosphere
        - name: Satellite data
          tag: Satellite data
        - name: Software
          tag: Software
        - name: Stars
          tag: Stars
        - name: Waves and modes
          tag: Waves and modes
    design:
      columns: 3
      fallback_icon: beaker
---
