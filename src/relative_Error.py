from cmath import nan
import numpy as np
import os


current_dir = os.getcwd()
script_dir = os.path.dirname(os.path.abspath(__file__))
python_sim_results = os.path.join(script_dir, 'output.txt')
matlab_sim_results = os.path.join(script_dir, 'output_matlab.txt')
# Load data from the Python simulation results file
py_data = np.loadtxt(python_sim_results)

# Load data from the Matlab simulation results file
matlab_data = np.loadtxt(matlab_sim_results)

# Extract the columns of interest (excluding the first column)
py_data_col1 = py_data[:, 1:]
matlab_data_col1 = matlab_data[:, 1:]

# Truncate the longer array to match the length of the shorter array
n_rows = min(py_data_col1.shape[0], matlab_data_col1.shape[0])
py_data_col1 = py_data_col1[:n_rows]
matlab_data_col1 = matlab_data_col1[:n_rows]

# Calculate the absolute difference between the corresponding columns
diff = np.abs(matlab_data_col1 - py_data_col1)

# Calculate the relative error
rel_error = np.divide(diff, matlab_data_col1, where=matlab_data_col1!=0)

# Print the maximum relative error for each column
max_rel_error = np.max(rel_error, axis=0)
print("Max relative error for each column:", max_rel_error)