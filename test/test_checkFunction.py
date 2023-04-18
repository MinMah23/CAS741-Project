import pytest
import numpy as np
from checkFunction import checkF

def test_checkF():
    # Test case 1: f is a float
    f = "3.0"
    t = 0
    assert checkF(f, t) == 3.0

    # Test case 2: f is a function
    f = "lambda t: 2*t"
    t = 1
    assert checkF(f, t) == 2.0