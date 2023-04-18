# odeM.py
# This module defines the equations of motion for the cart on a pendulum
import numpy as np
from constantM import GRAVITY
from checkFunction import checkF


def invertedPendulum(y, t, m_p, m_c, b_c, l_p, f):
    """Differential equations for a pendulum on a cart.

    Args:
        t (float): Current time.
        y (list): List of current values for [theta, theta_dot, x, x_dot].
        m_p (float): Mass of the pendulum.
        m_c (float): Mass of the cart.
        b_c (float): Friction of the cart.
        l_p (float): Length of the pendulum.
        f (function): Function that returns the external force applied to the cart as a function of time.

    Returns:
        list: List of the derivatives of [theta, theta_dot, x, x_dot] at the current time.
        Theta is the angle of the pendulum, theta_dot is the velocity of the pendulum while x is the position of the cart
        and x_dot is the derivative of the cart and its velocity. The accelaration of the pendulum and cart are caculated in ths module.
    """

    # Unpack the state variables
    # x is the position of cart, x_dot is the velocity of the cart
    # theta is the angle of the pendulum and theta_dot is the velocity of the pendulum
    # (x, xdot, theta, theta_dot)
    x, xdot, theta, theta_dot = y

    # Compute the sine and cosine of the pendulum angle
    sin_theta = np.sin(theta)
    cos_theta = np.cos(theta)

    # Calculate the inertia of the pendulum
    I_p = m_p * l_p ** 2

    # Check the function
    time_func = checkF(f, t)

    # Define the differential equations
    theta2dotdot = 0
    x2dotdot = 0
    x1dot = xdot
    x2dotdot = (1 / (m_c + m_p)) * ((time_func - b_c * xdot + m_p * l_p * theta_dot**2 * sin_theta) - (m_p * l_p * theta2dotdot * cos_theta))
    theta1dot = theta_dot
    theta2dotdot = (1 / I_p + (m_p * l_p**2)) * ((m_p * GRAVITY * l_p * sin_theta) - (m_p * l_p * x2dotdot * cos_theta))
    res = [x1dot, x2dotdot, theta1dot, theta2dotdot]

    return res
