# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt
import math
from astropy import constants as const
from astropy import units as u

# ========================== plotter function
def my_plotter(ax, data1, data2, xylabels, axestype, legendyes, **param_dict):
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
    if axestype == 0:
        ax.plot(data1, data2, **param_dict)
        ax.set_xlabel(xylabels[0])
        ax.set_ylabel(xylabels[1])
    if axestype == 1:
        ax.semilogy(data1, data2, **param_dict)
        ax.set_xlabel(xylabels[0])
        ax.set_ylabel(xylabels[1])
    if axestype == 2:
        ax.loglog(data1, data2, **param_dict)
        ax.set_xlabel(xylabels[0])
        ax.set_ylabel(xylabels[1])
    if legendyes:
        leg = ax.legend(loc=0, frameon=1, handlelength=5)
        frame = leg.get_frame()
        frame.set_facecolor("floralwhite")

    return


# ========================== read the data


def readdata(sink_file_name, simfolder):
    # time unit calculation
    timeUnit = (const.pc ** 3 / (const.G) / const.M_sun) ** (0.5)
    path = simfolder + sink_file_name

    time, x, y, z, mass = np.loadtxt(path, unpack=True, usecols=(0, 1, 2, 3, 4))
    time = time * timeUnit.to(u.year).value / 1.0e3  ## time in kyr
    time = time / 100.0  ## time in 100 kyr

    return time, x, y, z, mass


# ========================== do Mass vs Time plot
def plot_masstime(
    nsinkfiles,
    simfolder,
    sink_file_base,
    sink_file_tail,
    axestype,
    big_sink,
    both_sides,
    outputfig,
):
    ## plot properties

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
    xylabels = ["Time [100 kyr]", r"Mass [M$_\odot$]"]

    ##  create plot

    # fig, (ax1, ax2) = plt.subplots(1, 2)
    fig, ax1 = plt.subplots(1, 1)
    sink_file_list = []
    ii = range(1, nsinkfiles + 1)  # number of sink particles created in the simulation
    for _ in ii:
        strii = "{:04d}".format(_)
        sink_file_list.append(strii)
    for _ in sink_file_list:  # loop over sink files
        sink_file_name = sink_file_base + _ + sink_file_tail
        print(sink_file_name)
        time, x, y, z, mass = readdata(sink_file_name, simfolder)
        fz0 = math.fabs(z[0])  # if absolute value is used
        if both_sides:
            z0 = fz0
            zstr = "|z|"  # used for the line label in the legend
        else:
            z0 = z[0]
            zstr = "z"
        # decide which sink file must be considered
        if big_sink:
            if z0 >= 0.5:
                cc = "C0"
            elif z0 < 0.5 and z0 >= 0.4:
                cc = "C1"
            elif z0 < 0.4 and z0 >= 0.3:
                cc = "C2"
            elif z0 < 0.3 and z0 >= 0.2:
                cc = "C3"
            elif z0 < 0.2 and z0 >= 0.1:
                cc = "C4"
            elif z0 < 0.1 and z0 >= 0.0:
                cc = "C5"
            else:
                continue
        else:
            if z0 < 0.5 and z0 >= 0.4:
                cc = "C1"
            elif z0 < 0.4 and z0 >= 0.3:
                cc = "C2"
            elif z0 < 0.3 and z0 >= 0.2:
                cc = "C3"
            elif z0 < 0.2 and z0 >= 0.1:
                cc = "C4"
            elif z0 < 0.1 and z0 >= 0.0:
                cc = "C5"
            else:
                continue

        kwargs = {"label": "", "alpha": 0.5, "color": cc}
        my_plotter(
            ax1, time, mass, xylabels, axestype, legendyes=False, **kwargs
        )

    if big_sink:
        ccl = ["C0", "C1", "C2", "C3", "C4", "C5"]
        sinklabell = [
            "$" + zstr + " \geq 0.5$",
            "$0.4 \leq " + zstr + " < 0.5$",
            "$0.3 \leq " + zstr + " < 0.4$",
            "$0.2 \leq " + zstr + " < 0.3$",
            "$0.1 \leq " + zstr + " < 0.2$",
            "$0.0 \leq " + zstr + " < 0.1$",
        ]
    else:
        ccl = ["C1", "C2", "C3", "C4", "C5"]
        sinklabell = [
            "$0.4 \leq " + zstr + " < 0.5$",
            "$0.3 \leq " + zstr + " < 0.4$",
            "$0.2 \leq " + zstr + " < 0.3$",
            "$0.1 \leq " + zstr + " < 0.2$",
            "$0.0 \leq " + zstr + " < 0.1$",
        ]
    for i in range(0, len(ccl)):
        kwargs = {"label": sinklabell[i], "alpha": 0.5, "color": ccl[i]}
        my_plotter(ax1, [], [], xylabels, axestype, legendyes=True, **kwargs)

    plt.savefig(outputfig, dpi=400, bbox_inches="tight")
