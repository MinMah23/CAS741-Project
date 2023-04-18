import os
import constantM
from outputM import verify_output, write_output_to_file
from plotM import plot
from odeSolverM import solve
from inputM import read_inputs, verify_inputs, convert_inputs


def main():

    # Construct the path to the input file
    input_file = input("Please enter the name of input file: ")
    output_file = input("Please enter the name of output file: ")
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(script_dir, input_file)

    # Read input parameters
    with open(input_path, 'r') as fn:
        m_c, m_p, l_p, b_c, f, x_i, dx_i, theta_i, dtheta_i = read_inputs(fn)

    # Verify the inputs
    verify_inputs(m_c, m_p, l_p, b_c, f, x_i, dx_i, theta_i, dtheta_i)

    # Prepare the format of input values
    m_c, m_p, l_p, b_c, x_i, dx_i, theta_i, dtheta_i = convert_inputs(m_c, m_p, l_p, b_c, x_i, dx_i, theta_i, dtheta_i)

    # Define the initial state list of the system
    state0 = [x_i, dx_i, theta_i, dtheta_i]

    # Solve the ODEs
    sol = solve(m_p, m_c, b_c, l_p, f, state0, constantM.TSPAN)

    # Verify the output
    verify_output(sol)

    # Write output to file
    output_file = os.path.join(script_dir, output_file)
    write_output_to_file(output_file, sol, constantM.TSPAN)
    
    # Plot the results
    plot(constantM.TSPAN, sol)


if __name__ == '__main__':
    main()
