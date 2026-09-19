---
title: inermodz
weight: 9
summary: Python package to compute and display inertial modes of a sphere
date: '2024-01-01'
show_date: false
tags:
  - Software
links:
  - type: github
    url: 'https://github.com/AnkitBarik/inermodz'
    label: Code
---
A fluid rotating with solid body rotation (rotation rate {{<math>}}$\Omega${{</math>}}) is stably stratified in angular momentum. It can be shown that a small perturbation to this fluid gives rise to a wave solution that oscillates with frequency {{<math>}}$|\omega|\leq2\Omega${{</math>}}. In the absence of boundaries (or far away from them), such a wave propagates as plane waves called "inertial waves". In the presence of boundaries, the solution must satisfy boundary conditions (for example, impenetrability, {{<math>}}$\boldsymbol{u}\cdot\hat{\boldsymbol{n}}=0${{</math>}}) and the solutions are global modes called "inertial modes". These modes can be computed analytically for some container shapes such as a cylinder and a sphere. This python package allows one to compute the analytical mode frequencies and solutions in a sphere.