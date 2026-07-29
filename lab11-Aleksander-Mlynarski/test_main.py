from typing import Callable

import main
import numpy as np
import pytest
# Dill is used to deserialize the test data, including the functions
import dill

try:
    with open("expected", "rb") as f:
        expected = dill.load(f)
except (FileNotFoundError, dill.UnpicklingError):
    print(
        "Error: The 'expected' file was not found or is corrupted. Please regenerate it."
    )
    expected = {
        "rectangular_rule": [],
        "trapezoidal_rule": [],
        "custom_integration": [],
    }


# --- Data Preparation ---

valid_rectangular_rule = [
    (f, a, b, n, res) for f, a, b, n, res in expected["rectangular_rule"] if res is not None
]
valid_trapezoidal_rule = [
    (f, a, b, n, res) for f, a, b, n, res in expected["trapezoidal_rule"] if res is not None
]
valid_custom_integration = [
    (f, a, b, order, res) for f, a, b, order, res in expected["custom_integration"] if res is not None
]


# --- Tests for rectangular_rule ---

@pytest.mark.parametrize("func, a, b, n, expected_result", valid_rectangular_rule)
def test_rectangular_rule_correct_solution(
    func: Callable, a: float, b: float, n: int, expected_result: float
):
    """Tests if rectangular_rule calculates the correct integral value for valid inputs."""
    # 'func' is a callable function object loaded directly from the file
    actual_result = main.rectangular_rule(func, a, b, n)
    assert actual_result == pytest.approx(expected_result), (
        "The integral value from the rectangular rule is incorrect."
    )


# --- Tests for trapezoidal_rule ---

@pytest.mark.parametrize("func, a, b, n, expected_result", valid_trapezoidal_rule)
def test_trapezoidal_rule_correct_solution(
    func: Callable, a: float, b: float, n: int, expected_result: float
):
    """Tests if trapezoidal_rule calculates the correct integral value for valid inputs."""
    actual_result = main.trapezoidal_rule(func, a, b, n)
    assert actual_result == pytest.approx(expected_result), (
        "The integral value from the trapezoidal rule is incorrect."
    )


# --- Tests for custom_integration ---

@pytest.mark.parametrize("func, a, b, order, expected_result", valid_custom_integration)
def test_custom_integration_correct_solution(
    func: Callable, a: float, b: float, order: int, expected_result: float
):
    """Tests if custom_integration calculates the correct integral value for valid inputs."""
    actual_result = main.custom_integration(func, a, b, order)
    assert actual_result == pytest.approx(expected_result), (
        "The integral value from custom_integration (Gauss-Legendre) is incorrect."
    )