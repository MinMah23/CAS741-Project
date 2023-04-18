import pytest
import constantM
import inputM


@pytest.fixture
def valid_inputs():
    return (1.0, 2.0, 3.0, 0.1, "10*sin(t)", 1.0, 0.0, 0.1, 0.0)

def test_read_inputs(valid_inputs):
    with open("test_inputs.txt", "w") as f:
        f.write("test case\n")
        f.write(str(valid_inputs[0]) + "\n")
        f.write(str(valid_inputs[1]) + "\n")
        f.write(str(valid_inputs[2]) + "\n")
        f.write(str(valid_inputs[3]) + "\n")
        f.write(str(valid_inputs[4]) + "\n")
        f.write(str(valid_inputs[5]) + "\n")
        f.write(str(valid_inputs[6]) + "\n")
        f.write(str(valid_inputs[7]) + "\n")
        f.write(str(valid_inputs[8]) + "\n")
        f.write("end\n")
    with open("test_inputs.txt", "r") as f:
        m_c, m_p, l_p, b_c, f, x_i, dx_i, theta_i, dtheta_i = inputM.read_inputs(f)
    m_c, m_p, l_p, b_c, x_i, dx_i, theta_i, dtheta_i = inputM.convert_inputs(m_c, m_p, l_p, b_c, x_i, dx_i, theta_i, dtheta_i)
    input = m_c, m_p, l_p, b_c, f, x_i, dx_i, theta_i, dtheta_i
    assert input == valid_inputs

def test_verify_inputs_valid(valid_inputs):
    m_c, m_p, l_c, b_c, f, x_i, dx_i, theta_i, dtheta_i = valid_inputs
    assert inputM.verify_inputs(m_c, m_p, l_c, b_c, f, x_i, dx_i, theta_i, dtheta_i) is None

def test_verify_inputs_invalid_mass_cart():
    with pytest.raises(ValueError, match="Mass of cart is not valid."):
        inputM.verify_inputs(constantM.M_CMIN - 1, 2.0, 3.0, 0.1, "10*sin(t)", 1.0, 0.0, 0.1, 0.0)
    with pytest.raises(ValueError, match="Mass of cart is not valid."):
        inputM.verify_inputs(constantM.M_CMAX + 1, 2.0, 3.0, 0.1, "10*sin(t)", 1.0, 0.0, 0.1, 0.0)

def test_verify_inputs_invalid_mass_pendulum():
    with pytest.raises(ValueError, match="Mass of pendulum is not valid."):
        inputM.verify_inputs(1.0, constantM.M_PMIN - 1, 3.0, 0.1, "10*sin(t)", 1.0, 0.0, 0.1, 0.0)
    with pytest.raises(ValueError, match="Mass of pendulum is not valid."):
        inputM.verify_inputs(1.0, constantM.M_PMAX + 1, 3.0, 0.1, "10*sin(t)", 1.0, 0.0, 0.1, 0.0)

def test_verify_inputs_invalid_length_pendulum():
    with pytest.raises(ValueError, match="Length of pendulum is not valid."):
        inputM.verify_inputs(1.0, 2.0, constantM.L_PMIN - 1, 0.1, "10*sin(t)", 1.0, 0.0, 0.1, 0.0)
    with pytest.raises(ValueError, match="Length of pendulum is not valid."):
        inputM.verify_inputs(1.0, 2.0, constantM.L_PMAX + 1, 0.1, "10*sin(t)", 1.0, 0.0, 0.1, 0.0)

def test_verify_inputs_invalid_friction():
    with pytest.raises(ValueError, match="Friction of cart is not valid."):
        inputM.verify_inputs(1.0, 2.0, 3.0, -0.1, "10*sin(t)", 1.0, 0.0, 0.1, 0.0)
