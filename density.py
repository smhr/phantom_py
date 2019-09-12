# -*- coding: utf-8 -*-
"""
script to plot density profile of the filament 
in different simulation snapshots
"""
import numpy as np
from matplotlib import pyplot as plt


def my_plotter(ax, data1, data2, xylabels, **param_dict):
    """
    A helper function to make a graph

    Parameters
    ----------
    ax : Axes
        The axes to draw to

    data1 : array
       The x data

    data2 : array
       The y data

    param_dict : dict
       Dictionary of kwargs to pass to ax.plot
    """
    ax.loglog(data1, data2, **param_dict)
    ax.set_xlabel(xylabels[0])
    ax.set_ylabel(xylabels[1])
    leg = plt.legend(loc=0, frameon=1, handlelength=5)
    frame = leg.get_frame()
    frame.set_facecolor("floralwhite")

    return


# ==========================

data1, data2, data3, data4 = np.random.randn(4, 100)
r20, density20 = np.loadtxt(
    "../../runs/converge_test/M37N450rho14_new/density20.ev",
    unpack=True,
    usecols=(4, 5),
)
r30, density30 = np.loadtxt(
    "../../runs/converge_test/M37N450rho14_new/density30.ev",
    unpack=True,
    usecols=(4, 5),
)
r40, density40 = np.loadtxt(
    "../../runs/converge_test/M37N450rho14_new/density40.ev",
    unpack=True,
    usecols=(4, 5),
)
r50, density50 = np.loadtxt(
    "../../runs/converge_test/M37N450rho14_new/density50.ev",
    unpack=True,
    usecols=(4, 5),
)
plt.rc("text", usetex=True)
plt.rc("font", family="serif")
plt.style.use("bmh")
plt.style.use(
    {
        "axes.facecolor": "white",
        "xtick.direction": "out",
        "ytick.direction": "out",
        "xtick.top": "True",
        "ytick.right": "True",
    }
)
fig, ax = plt.subplots(1, 1)

xylabels = ["r [pc]", r"$\rho$ [g cm$^{-3}$]"]

kwargs = {"label": "t20", "alpha": 0.5}
my_plotter(ax, r20, density20, xylabels, **kwargs)

kwargs = {"label": "t30", "alpha": 0.5}
my_plotter(ax, r30, density30, xylabels, **kwargs)

kwargs = {"label": "t40", "alpha": 0.5}
my_plotter(ax, r40, density40, xylabels, **kwargs)

kwargs = {"label": "t50", "alpha": 0.5}
my_plotter(ax, r50, density50, xylabels, **kwargs)

plt.savefig("../../runs/converge_test/M37N450rho14.pdf", dpi=400, bbox_inches="tight")
