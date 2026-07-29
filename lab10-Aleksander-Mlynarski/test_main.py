import pickle
from typing import Any, Tuple

import main
import numpy as np
import pytest

try:
    with open("expected", "rb") as f:
        expected = pickle.load(f)
except FileNotFoundError:
    print(
        "Error: The 'expected' file was not found. Please ensure it is in the correct directory."
    )
    expected = {
        "linear_least_squares": [],
        "chebyshev_nodes": [],
    }


# --- Data Preparation ---

valid_linear_least_squares = [
    (x, y, res) for x, y, res in expected["linear_least_squares"] if res is not None
]
valid_chebyshev_nodes = [
    (n, interval, res) for n, interval, res in expected["chebyshev_nodes"] if res is not None
]


# --- Tests for linear_least_squares ---

@pytest.mark.parametrize("x, y, expected_result", valid_linear_least_squares)
def test_linear_least_squares_correct_solution(
    x: np.ndarray, y: np.ndarray, expected_result: np.ndarray
):
    """Tests if linear_least_squares calculates the correct coefficients for valid inputs."""
    actual_result = main.linear_least_squares(x, y)
    assert actual_result == pytest.approx(expected_result, abs=1e-5), (
        "Calculated coefficients for linear least squares are incorrect."
    )


# --- Tests for chebyshev_nodes ---

@pytest.mark.parametrize("n, interval, expected_result", valid_chebyshev_nodes)
def test_chebyshev_nodes_correct_solution(
    n: int, interval: Tuple[float, float], expected_result: np.ndarray
):
    """Tests if chebyshev_nodes calculates the correct nodes for valid inputs."""
    actual_result = main.chebyshev_nodes(n, interval)
    assert actual_result == pytest.approx(expected_result), (
        f"Chebyshev nodes are incorrect for n={n} and interval={interval}."
    )