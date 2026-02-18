"""
Tests for calculator module
"""
import pytest
from calculator import add, subtract, multiply, divide, calculate_average

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6

def test_divide():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    # This will expose the bug
    # pytest.raises(ZeroDivisionError, divide, 10, 0)

def test_calculate_average():
    assert calculate_average([1, 2, 3, 4, 5]) == 3
    assert calculate_average([10, 20]) == 15
    # This will expose the bug
    # pytest.raises(ValueError, calculate_average, [])
