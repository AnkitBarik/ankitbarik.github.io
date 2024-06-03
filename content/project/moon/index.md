---
title: Moon
summary: Explaining ancient lunar paleomagnetic records using a mix of convection and precession
tags:
  - Dynamos
date: '2017Z'
show_date: false

# Optional external URL for project (replaces project detail page).
external_link: ''

image:
  caption:
  focal_point: Smart
  preview_only: false

url_code: ''
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
Paleomagnetic analysis of rock samples returned from the Apollo missions have revealed that the Moon used to have a very strong magnetic field, higher than that of present day Earth 100{{< math >}}$\mu${{< /math >}}T, which then later dropped to values of around 10{{< math >}}$\mu${{< /math >}}T and eventually, at present day the moon does not generate any magnetic field.

![Lunar paleomagnetic record](lun_paleo.png)

The problem with generating such a strong magnetic field on the moon is the size of its core. A core of this size cannot have the amount of power needed to generate a magnetic field of this magnitude *at the surface*, keeping in mind that the core is very far away from the surface.

![Schematic of moon's interiors](Moon_int.png)

In addition, any dynamo mechanism attempting to explain the lunar paleomagnetic record must explain the following three things:

  - High magnetic field in the ancient past
  - Low magnetic field thereafter
  - No magnetic field in present day

A few different dynamo mechanisms have been proposed, each with their pros and cons:

  - Thermochemical convection:
    - Field intensity : low :x:
    - Lifetime : long :white_check_mark:
  - Basal magma ocean:
    - Field intensity : high :white_check_mark:
    - Lifetime: limited :white_check_mark:
    - Requires high magma conductivity :question:
  - Mechanical driving (e.g.: precession):
    - Field intensity : high :white_check_mark:
    - Lifetime: limited :white_check_mark:
    - Very hard to run simulations and scale to real values :x:

We followed a slightly different approach and found that a mix of convection and precession has the potential to explain all three features of the lunar paleomagnetic record.