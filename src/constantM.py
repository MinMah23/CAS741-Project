# constantM.py
# This module includes all the constant needed in the Inverted Pendulum Simulation

import numpy as np

GRAVITY = 9.81

# Define the valid values for the inputs
M_PMIN = 0.01  # kg
M_PMAX = 50  # kg
M_CMIN = 0.01  # kg
M_CMAX = 50  # kg
L_PMIN = 0.01  # metre
L_PMAX = 10  # metre

# Set up time array for running the simulation
T0 = 0   # the start time of the simulation
TF = 10   # the end time of the simulation
INTERVAL = 50000 # the whole space in th etime of simulation
TSPAN = np.linspace(T0, TF, INTERVAL)
