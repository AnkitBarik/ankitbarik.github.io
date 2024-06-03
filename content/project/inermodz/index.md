---
title: inermodz
summary: Python package to compute and display inertial modes of a sphere
tags:
  - Software
date: '2024Z'
show_date: false

# Optional external URL for project (replaces project detail page).
external_link: ''

image:
  caption: The {{< math >}}$(5,4)${{< /math >}} inertial mode
  focal_point: Smart

url_code: 'https://github.com/AnkitBarik/inermodz'
url_pdf: ''
url_slides: ''
url_video: ''

---
A fluid rotating with solid body rotation (rotation rate {{<math>}}$\Omega${{</math>}}) is stably stratified in angular momentum. It can be shown that a small perturbation to this fluid gives rise to a wave solution that oscillates with frequency {{<math>}}$|\omega|\leq2\Omega${{</math>}}. In the absence of boundaries (or far away from them), such a wave propagates as plane waves called "inertial waves". In the presence of boundaries, the solution must satisfy boundary conditions (for example, impenetrability, {{<math>}}$\boldsymbol{u}\cdot\hat{\boldsymbol{n}}=0${{</math>}}) and the solutions are global modes called "inertial modes". These modes can be computed analytically for some container shapes such as a cylinder and a sphere. This python package allows one to compute the analytical mode frequencies and solutions in a sphere.