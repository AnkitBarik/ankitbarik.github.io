---
title: Scientific Software
weight: 4
summary: Open-source codes I build and maintain for simulating and analyzing planetary and stellar magnetohydrodynamics.
show_date: false
tags:
  - Software
  - Dynamos
  - Waves and modes
  - Magnetosphere
---

Simulating and analyzing planetary and stellar magnetohydrodynamics requires purpose-built tools. Here are the codes and packages I develop and maintain.

## MagIC

MagIC is a numerical code that can simulate fluid dynamics in spherical geometry. It solves for the Navier-Stokes equation including Coriolis force, optionally coupled with an induction equation for Magneto-Hydro Dynamics (MHD), a temperature (or entropy) equation and an equation for chemical composition under both the anelastic and the Boussinesq approximations.

MagIC has been used in **174 publications** (170 refereed) since 2002, according to [NASA ADS](https://ui.adsabs.harvard.edu/public-libraries/LVt1vdaKQsC5P09In2iloA).

MagIC is pseudo-spectral and makes use of spherical harmonics {{<math>}}$Y_\ell^m(\theta,\phi)${{</math>}} in the angular directions. In the radial direction, it offers two options: one can either make use of Chebyshev polynomials or finite differences.

I am one of the developers of MagIC, so feel free to reach out if you plan to use it for your work! For more information, visit: https://magic-sph.github.io/ .

**Links:** [GitHub](https://github.com/magic-sph/magic) · [Publication metrics (ADS)](https://ui.adsabs.harvard.edu/public-libraries/LVt1vdaKQsC5P09In2iloA)
{style="text-align: justify;"}

## Kore

Kore is a numerical code that can solve for wave-like solutions in rotating spheres and spherical shells. It solves for solutions to the combination of *linearized* Navier-Stokes, magnetic induction equation, a temperature (or entropy) equation and an equation for chemical composition under both the anelastic and the Boussinesq approximations.
{style="text-align: justify;"}

Kore is fully spectral and makes use of spherical harmonics {{<math>}}$Y_\ell^m(\theta,\phi)${{</math>}} in the angular directions. In the radial direction, it expands every spherical harmonic coefficient in Chebyshev polynomials while using Gegenbauer polynomials to compute radial derivatives.
{style="text-align: justify;"}

I am one of the developers of Kore, so feel free to reach out if you plan to use it for your work! Kore is free and open source.
{style="text-align: justify;"}

**Links:** [GitHub](https://github.com/repepo/kore)

## Kaiju

Kaiju (formerly GAMERA) is written in modern Fortran and provides a flexible, portable, and exascale-capable MHD code. It uses the finite volume method to simulate magnetospheric dynamics.
{style="text-align: justify;"}

I was involved in adapting it to [Mercury](/project/unpublished/#external-fields-mercury) in order to accurately compute the field-aligned currents (FACs) and better correct the MESSENGER data.
{style="text-align: justify;"}

**Links:** [GitHub](https://github.com/JHUAPL/kaiju)

## planetMagFields

`planetMagFields` is a package that provides an easy interface to plot and analyze planetary magnetic field data. It provides very easy access to the Gauss coefficients of a planet's magnetic field obtained from inversion of planetary mission data, and an easy interface to plot, analyze and even produce files for 3D visualization of a planet's magnetic field.

To learn more, check out the documentation here: https://ankitbarik.github.io/planetMagFields/

If you're using this package for your work, please cite the paper in Journal of Open Source Software (JOSS):

  >Barik et al., (2024). planetMagFields: A Python package for analyzing and plotting planetary magnetic field data. Journal of Open Source Software, 9(97), 6677, https://doi.org/10.21105/joss.06677

  Or bibtex:

  ```bibtex
   @article{Barik2024,
      doi = {10.21105/joss.06677},
      url = {https://doi.org/10.21105/joss.06677},
      year = {2024},
      publisher = {The Open Journal},
      volume = {9},
      number = {97},
      pages = {6677},
      author = {Barik, Ankit and Angappan, Regupathi},
      title = {planetMagFields: A Python package for analyzing and plotting planetary magnetic field data},
      journal = {Journal of Open Source Software}
   }
  ```

**Links:** [Try the app](https://planetmagfields.streamlit.app) · [GitHub](https://github.com/AnkitBarik/planetMagFields) · [Read paper](https://doi.org/10.21105/joss.06677)

## inermodz

A fluid rotating with solid body rotation (rotation rate {{<math>}}$\Omega${{</math>}}) is stably stratified in angular momentum. It can be shown that a small perturbation to this fluid gives rise to a wave solution that oscillates with frequency {{<math>}}$|\omega|\leq2\Omega${{</math>}}. In the absence of boundaries (or far away from them), such a wave propagates as plane waves called "inertial waves". In the presence of boundaries, the solution must satisfy boundary conditions (for example, impenetrability, {{<math>}}$\boldsymbol{u}\cdot\hat{\boldsymbol{n}}=0${{</math>}}) and the solutions are global modes called "inertial modes". These modes can be computed analytically for some container shapes such as a cylinder and a sphere. This Python package allows one to compute the analytical mode frequencies and solutions in a sphere.

**Links:** [GitHub](https://github.com/AnkitBarik/inermodz)
