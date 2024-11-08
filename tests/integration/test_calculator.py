import pytest

import calculator


def test_calculator_operations():
    # Test the full calculator package
    result = calculator.add(
        calculator.multiply(2, 3),
        calculator.divide(10, 2)
    )
    assert result == 11

    result = calculator.subtract(
        calculator.add(5, 5),
        calculator.multiply(2, 2)
    )
    assert result == 6

def test_version():
    assert hasattr(calculator, '__version__')
    assert isinstance(calculator.__version__, str)