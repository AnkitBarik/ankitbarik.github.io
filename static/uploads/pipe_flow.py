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

dpdx = -7
mu = 0.1

R = 1
x = np.array([5*R])
y = np.linspace(-R,R,20)

x2d,y2d = np.meshgrid(x,y,indexing='ij')

u = (y**2 - R**2)/(4*mu) * dpdx
v = np.zeros_like(u)

fig,ax = plt.subplots(figsize=(12,12))

quiv = ax.quiver(x2d,y2d,u,v,u,scale_units='xy',scale=5,cmap='plasma')

ax.set_xlim(0,10*R)
ax.set_xlabel(r'$z$',fontsize=40)
ax.set_ylabel(r'$s$',fontsize=40)
ax.tick_params(labelsize=20)

cbar = fig.colorbar(quiv,aspect=40)
cbar.ax.tick_params(labelsize=20)
cbar.ax.set_ylabel(r'$u$',fontsize=40)

plt.tight_layout()
plt.show()
