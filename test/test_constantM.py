import constantM

def test_constants():
    # Check if GRAVITY is equal to 9.81
    assert constantM.GRAVITY == 9.81

    # Check if valid input values are within expected ranges
    assert constantM.M_PMIN > 0
    assert constantM.M_PMAX <= 50
    assert constantM.M_CMIN > 0
    assert constantM.M_CMAX <= 50
    assert constantM.L_PMIN > 0
    assert constantM.L_PMAX <= 10

    # Check if time array parameters are valid
    assert constantM.T0 < constantM.TF