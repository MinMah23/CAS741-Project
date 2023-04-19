from inputM import verify_inputs, convert_inputs
from outputM import verify_output
from odeSolverM import solve
from plotM import plot
import constantM
import pytest
import os

@pytest.fixture
def file_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, 'inputs.txt')
    return input_path

def test_all(file_path):
        with open(file_path, 'r') as f:
            lines = f.readlines()
            for i in range(0, len(lines), 11):
                startString = lines[i]
                m_c = float(lines[i+1])
                m_p = float(lines[i+2])
                l_p = float(lines[i+3])
                b_c = float(lines[i+4])
                f = lines[i+5]
                x_i = float(lines[i+6])
                dx_i = float(lines[i+7])
                theta_i = float(lines[i+8])
                dtheta_i = float(lines[i+9])
                endString = lines[i+10]
                
                verify_inputs(m_c, m_p, l_p, b_c, f, x_i, dx_i, theta_i, dtheta_i)

                # Prepare the format of input values
                m_c, m_p, l_p, b_c, x_i, dx_i, theta_i, dtheta_i = convert_inputs(m_c, m_p, l_p, b_c, x_i, dx_i, theta_i, dtheta_i)

                # Define the initial state list of the system
                state0 = [x_i, dx_i, theta_i, dtheta_i]

                # Solve the ODEs
                sol = solve(m_p, m_c, b_c, l_p, f, state0, constantM.TSPAN)

                # Verify the output
                verify_output(sol)

                # Plot the results
                plot(constantM.TSPAN, sol)