---
title: MagIC
summary: High-performance code that solves the magneto-hydrodynamics equations in rotating spherical shells
tags:
  - Dynamos
  - software
date:
show_date: false

# Optional external URL for project (replaces project detail page).
external_link: ''

image:
  caption:
  focal_point: Smart
  preview_only: false

url_code: 'https://github.com/magic-sph/magic'
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

MagIC is a numerical code that can simulate fluid dynamics in spherical geometry. It solves for the Navier-Stokes equation including Coriolis force, optionally coupled with an induction equation for Magneto-Hydro Dynamics (MHD), a temperature (or entropy) equation and an equation for chemical composition under both the anelastic and the Boussinesq approximations.

MagIC is pseudo-spectral and makes use of spherical harmonics {{<math>}}$Y_\ell^m(\theta,\phi)${{</math>}} in the angular directions. In the radial direction, it offers two options : one can either make use of Chebyshev polynomials or finite differences.

I am one of the developers of MagIC, so feel free to reach out if you plan to use it for your work!

For more information, visit: https://magic-sph.github.io/ .
{style="text-align: justify;"}