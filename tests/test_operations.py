# tests/test_operations.py
from src.calculator.operations import Calculator

import pytest


def test_add():
    assert Calculator.add(2, 3) == 5
    assert Calculator.add(-1, 1) == 0


def test_subtract():
    assert Calculator.subtract(5, 3) == 2
    assert Calculator.subtract(1, 1) == 0


def test_multiply():
    assert Calculator.multiply(2, 3) == 6
    assert Calculator.multiply(-2, 3) == -6


def test_divide():
    assert Calculator.divide(6, 2) == 3
    assert Calculator.divide(5, 2) == 2.5
    with pytest.raises(ValueError):
        Calculator.divide(5, 0)

