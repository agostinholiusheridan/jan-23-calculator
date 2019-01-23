"""
If given 2 and 2 as parameters, 4 should be returned.
"""
from calculator import add
import pytest

def test_two_plus_two():
    assert add(3, 3) == 6

def test_one_two_three():
    assert add(1,2,3) == 6

def test_negative_values():
    "assert negative values that works"

def test_negative_values3():
"""
0.1 are float type
"""
    assert round(add(0.1,0.1,0.1),2) ==pytest.approx(0.3)
