# outputM.pt
# This module write the angle and velocity of pendullum plus the position and
# velocity of the cart at the corresponding time atthe output file
import numpy as np


def verify_output(solution):
    x = solution[:, 0]
    theta = solution[:, 2]
    for i in range(0,len(x)):
        if not (x[i] >= 0):
            raise ValueError("The calculated value of position of the cart is not valid.")
    for j in range(0,len(theta)):
        if not (0 <= theta[j] <= 2 * np.pi):
            raise ValueError("The calculated value of angle of the pendulum is not valid.")

def write_output_to_file(output_file, sol, time):

    # Extract the results
    t = time.reshape(-1, 1)
    xp = sol[:, 0].reshape(-1, 1)
    xdot = sol[:, 1].reshape(-1, 1)
    theta = sol[:, 2].reshape(-1, 1)
    thetadot = sol[:, 3].reshape(-1, 1)

    # Combine the columns into a single array
    # x x_dot theta theta_dot
    data = np.column_stack((t, xp, xdot, theta, thetadot))

    # Save the data to a file
    np.savetxt(output_file, data, fmt='%.4f', delimiter=' ')
