#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt

plotStyle = 'dark'

if plotStyle == 'dark':
    plt.style.use("dark_background")
    plt.rcParams.update({
        "axes.facecolor"   : "#1b1b1b",
        "figure.facecolor" : "#1b1b1b",
        "figure.edgecolor" : "#1b1b1b",
        "savefig.facecolor": "#1b1b1b",
        "savefig.edgecolor": "#1b1b1b"})


r1 = 0.5
r2 = 1
Omega1 = -5
Omega2 = 10

s = np.linspace(r1,r2,100)
phi = np.linspace(0,2*np.pi,100)

denom = r2**2 - r1**2

A = (Omega2 * r2**2 - Omega1 * r1**2)/denom
B = (Omega1 - Omega2) * r1**2 * r2**2/denom

s2d,p2d = np.meshgrid(s,phi)

uphi = A*s2d + B/s2d
us = np.zeros_like(uphi)

ke = 0.5*uphi**2

fig,ax = plt.subplots(figsize=(12,12),subplot_kw={'projection': 'polar'})

if Omega1*Omega2 < 0:
    cmap='PuOr_r'
else:
    cmap='plasma'

strm = ax.streamplot(phi,s,uphi.transpose()/s2d.transpose(),us.transpose(),cmap=cmap,color=uphi.transpose(),density=[10,0.4])
ax.set_ylim(0,r2)
ax.set_aspect('equal')
ax.grid(False)
ax.set_xticks([])
ax.set_yticks([r1,r2])
ax.tick_params(labelsize=20)
cbar = fig.colorbar(strm.lines)
cbar.ax.tick_params(labelsize=20)
plt.tight_layout()
plt.show()
