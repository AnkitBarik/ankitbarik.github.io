---
# Suppress only this section's own list page (no standalone "/teaching/" archive);
# individual notes below still render normally and are linked from the homepage.
build:
  render: never

# Hide the author bio box at the bottom of each note's detail page.
cascade:
  - params:
      profile: false
---
