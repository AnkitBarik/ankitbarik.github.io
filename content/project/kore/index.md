---
title: Kore
summary: High performance code that solves the linearized magneto-hydrodynamics equations in rotating spherical shells
tags:
  - Waves and modes
  - software
date:
show_date: false

# Optional external URL for project (replaces project detail page).
external_link: ''

image:
  caption:
  focal_point: Smart
  preview_only: false

url_code: 'https://github.com/repepo/kore'
url_pdf: ''
url_slides: ''
url_video: ''

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides: example
---

Kore is a numerical code that can solves for wave-like solutions in rotating spheres and spherical shells. It solves for solutions to the combination of *linearized* Navier-Stokes, magnetic induction equation, a temperature (or entropy) equation and an equation for chemical composition under both the anelastic and the Boussinesq approximations.
{style="text-align: justify;"}

Kore is fully spectral and makes use of spherical harmonics {{<math>}}$Y_\ell^m(\theta,\phi)${{</math>}} in the angular directions. In the radial direction, it expands every spherical harmonic coefficient in Chebyshev polynomials while using Gegenbauer polynomials to compute radial derivatives.
{style="text-align: justify;"}

I am one of the developers of Kore, so feel free to reach out if you plan to use it for your work! Kore is free and open source and is available at :  https://github.com/repepo/kore .
{style="text-align: justify;"}