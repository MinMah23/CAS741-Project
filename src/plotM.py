# plotM.py
# This module generates two graphs of cart position
# and angle of pendulum over time


import matplotlib.pyplot as plt


def plot(t, sol):

    # Extract the result 
    x = sol[:, 0]
    theta = sol[:, 2]
    # Plot the results
    fig, axs = plt.subplots(2, 1, figsize=(8, 8))

    # Cart position plot
    axs[0].plot(t, x, 'b')
    axs[0].set_ylabel('Cart position (m)')

    # Pendulum angle plot
    axs[1].plot(t, theta, 'r')
    axs[1].set_ylabel('Pendulum angle (rad)')
    axs[1].set_xlabel('Time (s)')

    plt.show()
