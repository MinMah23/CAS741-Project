# odeSolverM.py
# This module solve the equations that odeM generated
# and calculated the position of cart and the angle of pendulum

from odeM import invertedPendulum
from scipy.integrate import odeint
import numpy as np


def solve(m, M, b, L, f, state0, tspan):

    # Solve the ODEs using odeint
    sol = odeint(invertedPendulum, state0, tspan, args=(m, M, b, L, f))
    sol= abs(sol)
    print(max(sol[:, 2]))
    sol[:, 2] = np.divide(sol[:, 2], 2*np.pi)
    return sol
