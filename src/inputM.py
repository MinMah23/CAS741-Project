# inputM.py
# This module read all the inputs from input file and stores them
# And the verify_input checks all the constraints on inputs
import constantM
import numpy as np


def read_inputs(file):

    data = file.readlines()
    if (data[0].strip()== "test case"):
        m_c = data[1].strip()  # Mass of the cart
        m_p = data[2].strip()  # Mass of the pendulum
        l_c = data[3].strip()  # Length of the pendulum
        b_c = data[4].strip()  # Friction coefficient
        f = data[5].strip()   # External force applied to the cart
        x_i = data[6].strip()  # Initial value for position of cart
        dx_i = data[7].strip()  # Initial value for cart velocity
        theta_i = data[8].strip()  # Initial value for angle of the pendulum
        dtheta_i = data[9].strip() # Initial value for velocity of the pendulum
        end = data[10].strip()
    return m_c, m_p, l_c, b_c, f, x_i, dx_i, theta_i, dtheta_i


# Check input values for validity
def verify_inputs(m_c, m_p, l_p, b_c, f, x_i, dx_i, theta_i, dtheta_i):

    # Verify mass of cart
    if m_c == "" or not (constantM.M_CMIN <= float(m_c) <= constantM.M_CMAX):
        raise ValueError("Mass of cart is not valid.")

    # Verify mass of pendulum
    if m_p == "" or not (constantM.M_PMIN <= float(m_p) <= constantM.M_PMAX):
        raise ValueError("Mass of pendulum is not valid.")

    # Verify length of pendulum
    if l_p == "" or not (constantM.L_PMIN <= float(l_p) <= constantM.L_PMAX):
        raise ValueError("Length of pendulum is not valid.")

    if b_c == "" or not (float(b_c) >= 0):
        raise ValueError("Friction of cart is not valid.")

    if x_i == "" or not (float(x_i) >= 0):
        raise ValueError("Initial value for position of cart is not valid.")
    
    if dx_i == "" or not (float(dx_i) >= 0):
        raise ValueError("Initial value for cart velocity is not valid.")

    if theta_i == "" or not (0 <= float(theta_i) <= 2 * np.pi):
        raise ValueError("Initial value for angle of the pendulum is not valid.")

    if dtheta_i == "" or not (float(dtheta_i) >= 0):
        raise ValueError("Initial value for velocity of the pendulum is not valid.")

# Convert inouts to valid format
def convert_inputs(m_c, m_p, l_p, b_c, x_i, dx_i, theta_i, dtheta_i):
    m_c = float(m_c)
    m_p = float(m_p)
    l_p = float(l_p)
    b_c = float(b_c)
    x_i = float(x_i)
    dx_i = float(dx_i)
    theta_i = float(theta_i)
    dtheta_i = float(dtheta_i)
    return m_c, m_p, l_p, b_c, x_i, dx_i, theta_i, dtheta_i