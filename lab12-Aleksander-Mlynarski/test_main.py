from typing import Callable

import main
import numpy as np
import pytest
import dill

try:
    with open("expected", "rb") as f:
        expected = dill.load(f)
except (FileNotFoundError, dill.UnpicklingError):
    print(
        "Error: The 'expected' file was not found or is corrupted. Please regenerate it."
    )
    expected = {
        "arenstorf": [],
        "solve_euler": [],
    }


# --- Data Preparation ---

valid_arenstorf = [
    (t, x, res) for t, x, res in expected["arenstorf"] if res is not None
]
valid_solve_euler = [
    (func, t_span, y0, res) for func, t_span, y0, res in expected["solve_euler"] if res is not None
]


# --- Tests for arenstorf ---

@pytest.mark.parametrize("t, x, expected_result", valid_arenstorf)
def test_arenstorf_correct_solution(
    t: float, x: np.ndarray, expected_result: np.ndarray
):
    """Tests if arenstorf calculates the correct derivatives for a given state."""
    actual_result = main.arenstorf(t, x)
    assert actual_result == pytest.approx(expected_result), (
        "The calculated derivatives for the Arenstorf orbit are incorrect."
    )


# --- Tests for solve_euler ---

@pytest.mark.parametrize("func, t_span, y0, expected_result", valid_solve_euler)
def test_solve_euler_correct_solution(
    func: Callable, t_span: np.ndarray, y0: np.ndarray, expected_result: np.ndarray
):
    """Tests if solve_euler correctly solves an ODE system for valid inputs."""
    actual_result = main.solve_euler(func, t_span, y0)
    assert actual_result == pytest.approx(expected_result), (
        "The solution matrix from the Euler solver is incorrect."
    )