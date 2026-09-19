---
title: Kore
weight: 2
summary: High performance code that solves the linearized magneto-hydrodynamics equations in rotating spherical shells
show_date: false
tags:
  - Waves and modes
  - Software
links:
  - type: github
    url: 'https://github.com/repepo/kore'
    label: Code
---

Kore is a numerical code that can solves for wave-like solutions in rotating spheres and spherical shells. It solves for solutions to the combination of *linearized* Navier-Stokes, magnetic induction equation, a temperature (or entropy) equation and an equation for chemical composition under both the anelastic and the Boussinesq approximations.
{style="text-align: justify;"}

Kore is fully spectral and makes use of spherical harmonics {{<math>}}$Y_\ell^m(\theta,\phi)${{</math>}} in the angular directions. In the radial direction, it expands every spherical harmonic coefficient in Chebyshev polynomials while using Gegenbauer polynomials to compute radial derivatives.
{style="text-align: justify;"}

I am one of the developers of Kore, so feel free to reach out if you plan to use it for your work! Kore is free and open source and is available at :  https://github.com/repepo/kore .
{style="text-align: justify;"}