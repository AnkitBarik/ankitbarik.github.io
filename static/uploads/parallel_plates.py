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

U = 10
dpdx = -2.

# U = 5
# dpdx = 5.

# Plane Couette
#--------------

# U = 10
# dpdx = 0.

# Plane Poiseuille flow
# ---------------------

# U = 0
# dpdx = -5

mu = 0.1

L = 1
x = np.array([5*L])
y = np.linspace(0,L,20)

x2d,y2d = np.meshgrid(x,y,indexing='ij')

u = U*y2d/L + 0.5*y2d/mu * dpdx  * (y2d-L)
v = np.zeros_like(u)

fig,ax = plt.subplots(figsize=(12,12))

if u.max()*u.min() < 0:
    cmap = 'PuOr_r'
else:
    cmap = 'plasma'

quiv = ax.quiver(x2d,y2d,u,v,u,scale_units='xy',scale=5,cmap=cmap)

ax.set_xlim(0,10*L)
ax.set_xlabel(r'$x$',fontsize=40)
ax.set_ylabel(r'$y$',fontsize=40)
ax.tick_params(labelsize=20)

cbar = fig.colorbar(quiv,aspect=40)
cbar.ax.tick_params(labelsize=20)
cbar.ax.set_ylabel(r'$u$',fontsize=40)

plt.tight_layout()
plt.show()
