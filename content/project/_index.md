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
    design:
      view: article-grid
      columns: 3
      fallback_icon: beaker
---
