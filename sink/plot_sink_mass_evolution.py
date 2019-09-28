# -*- coding: utf-8 -*-
from sink import plot_masstime
from astropy import constants as const
from astropy import units as u
import numpy as np
#import math

# time unit calculation
timeUnit = (const.pc ** 3 / (const.G) / const.M_sun) ** (0.5)
print("\n The unit of time in the simulation is ", timeUnit.to(u.year).value / 1.0e3, " kyr")

filamentM = 50*u.solMass #filament mass
filamentL = 1.5*u.pc #filament length
filamentR = 0.1*u.pc #filament radius
filamentV = np.pi*filamentR**2.*filamentL
filamentDens = filamentM/filamentV #filament density
print("The filament density is ", filamentDens, "\n or")
filamentDens = filamentDens.decompose(u.cgs.bases)
print(filamentDens, "\n")
#tfreefall = np.sqrt((3.*np.pi)/(32.*filamentDens)) ## in second but without unit
#tfreefall = tfreefall*u.s ## get it the second unit again
#tfreefall = tfreefall.to(u.year)
#print("The free-fall time at the onset of simulation is",tfreefall.to(u.s))
#print("********************************\n")


# ========================== variables

nsinkfiles = 6  # number of sink files that should be plotted

simfolder = "../../../runs/M37A0/"  # simulation folder that contains sink.ev files.

sink_file_base = "N300M37rho17hac120Sink"

sink_file_tail = "N01.ev"
axestype = 0  # 0: no log; 1: semilogy; 2: loglog

big_sink = 0  # If True, the big sink is also plotted
both_sides = 0 # If True, both sides of the filament (|z|<filament length) is considered  

if big_sink:
    # where the figure should be saved?
    outputfig = "../../../runs/N300_sink_plot/M37A0SinkMassVsTimeAll.png"
else:
    outputfig = "../../../runs/N300_sink_plot/M37A0SinkMassVsTime.png"

# =========================== M37A0rho17
#plot_masstime(
#    nsinkfiles,
#    simfolder,
#    sink_file_base,
#    sink_file_tail,
#    axestype,
#    big_sink,
#    both_sides,
#    outputfig,
#)
# =========================== M50A0rho17
#nsinkfiles = 54
#simfolder = "../../../runs/M50A0/"
#sink_file_base = "N300M50rho17hac120Sink"
#if big_sink:
#    outputfig = "../../../runs/N300_sink_plot/M50A0SinkMassVsTimeAll.png"
#else:
#    outputfig = "../../../runs/N300_sink_plot/M50A0SinkMassVsTime.png"
#plot_masstime(
#    nsinkfiles,
#    simfolder,
#    sink_file_base,
#    sink_file_tail,
#    axestype,
#    big_sink,
#    both_sides,
#    outputfig,
#)
# =========================== M50N450rho15
nsinkfiles = 72
simfolder = "../../../runs/converge_test/M50N450rho15_new/"
sink_file_base = "N450M50rho15hac120Sink"
if big_sink:
    outputfig = "../../../runs/converge_test/M50N450rho15SinkMassVsTimeAll.png"
else:
    outputfig = "../../../runs/converge_test/M50N450rho15SinkMassVsTime.png"
plot_masstime(
    nsinkfiles,
    simfolder,
    sink_file_base,
    sink_file_tail,
    axestype,
    big_sink,
    both_sides,
    outputfig,
)
# =========================== M37N450rho15
nsinkfiles = 92
simfolder = "../../../runs/converge_test/M37N450rho15_new/"
sink_file_base = "N450M37rho15hac120Sink"
if big_sink:
    outputfig = "../../../runs/converge_test/M37N450rho15SinkMassVsTimeAll.png"
else:
    outputfig = "../../../runs/converge_test/M37N450rho15SinkMassVsTime.png"
plot_masstime(
    nsinkfiles,
    simfolder,
    sink_file_base,
    sink_file_tail,
    axestype,
    big_sink,
    both_sides,
    outputfig,
)
# =========================== M37N450rho14
nsinkfiles = 100
simfolder = "../../../runs/converge_test/M37N450rho14_new/"
sink_file_base = "N450M37rho14hac120Sink"
if big_sink:
    outputfig = "../../../runs/converge_test/M37N450rho14SinkMassVsTimeAll.png"
else:
    outputfig = "../../../runs/converge_test/M37N450rho14SinkMassVsTime.png"
plot_masstime(
    nsinkfiles,
    simfolder,
    sink_file_base,
    sink_file_tail,
    axestype,
    big_sink,
    both_sides,
    outputfig,
)