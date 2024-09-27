import pytest
from calculator import Calculator

@pytest.fixture
def setup_calculator():
    # Ensure history is cleared before each test
    Calculator.clear_history()

def test_add(setup_calculator):
    result = Calculator.add(3, 2)
    assert result == 5

def test_subtract(setup_calculator):
    result = Calculator.subtract(5, 2)
    assert result == 3

def test_multiply(setup_calculator):
    result = Calculator.multiply(3, 2)
    assert result == 6

def test_divide(setup_calculator):
    result = Calculator.divide(6, 2)
    assert result == 3

def test_divide_by_zero(setup_calculator):
    with pytest.raises(ZeroDivisionError):
        Calculator.divide(6, 0)

def test_last_calculation(setup_calculator):
    Calculator.add(3, 2)
    last_calc = Calculator.get_last_calculation()
    assert last_calc.get_result() == 5

def test_history(setup_calculator):
    Calculator.add(3, 2)
    Calculator.subtract(5, 2)
    assert len(Calculator.get_history()) == 2
