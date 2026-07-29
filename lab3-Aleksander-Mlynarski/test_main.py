# -*- coding: utf-8 -*-

import pytest
import main
import pickle
import math
import numpy as np

with open("expected", "rb") as f:
    test_cases = pickle.load(f)


@pytest.mark.parametrize("v,v_approx,result", test_cases["absolute_error"])
def test_absolute_error(v: int, v_approx: int | float, result):
    if np.any(np.isnan(result)):
        assert np.isnan(main.absolute_error(v, v_approx)), (
            "Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.".format(
                result, main.absolute_error(v, v_approx)
            )
        )
    else:
        assert main.absolute_error(v, v_approx) == pytest.approx(result), (
            "Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.".format(
                result, main.absolute_error(v, v_approx)
            )
        )


@pytest.mark.parametrize("v,v_approx,result", test_cases["relative_error"])
def test_relative_error(v: int, v_approx: int | float, result):
    if np.any(np.isnan(result)):
        assert np.isnan(main.relative_error(v, v_approx)), (
            "Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.".format(
                result, main.relative_error(v, v_approx)
            )
        )
    else:
        assert main.relative_error(v, v_approx) == pytest.approx(result), (
            "Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.".format(
                result, main.relative_error(v, v_approx)
            )
        )


@pytest.mark.parametrize("n,c,result", test_cases["p_diff"])
def test_p_diff(n: int, c: int | float, result):
    if np.any(np.isnan(result)):
        assert math.isnan(main.p_diff(n, c)), (
            "Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.".format(
                result, main.p_diff(n, c)
            )
        )
    else:
        assert main.p_diff(n, c) == pytest.approx(result), (
            "Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.".format(
                result, main.p_diff(n, c)
            )
        )


@pytest.mark.parametrize("x,n,result", test_cases["exponential"])
def test_exponential(x: int | float, n: int, result):
    if np.any(np.isnan(result)):
        assert np.isnan(main.exponential(x, n)), (
            "Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.".format(
                result, main.exponential(x, n)
            )
        )
    else:
        assert main.exponential(x, n) == pytest.approx(result), (
            "Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.".format(
                result, main.exponential(x, n)
            )
        )


@pytest.mark.parametrize("k,x,result", test_cases["coskx1"])
def test_coskx1(k: int, x: int | float, result):
    if np.any(np.isnan(result)):
        assert np.isnan(main.coskx1(k, x)), (
            "Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.".format(
                result, main.coskx1(k, x)
            )
        )
    else:
        assert main.coskx1(k, x) == pytest.approx(result), (
            "Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.".format(
                result, main.coskx1(k, x)
            )
        )


@pytest.mark.parametrize("k,x,result", test_cases["coskx2"])
def test_coskx2(k: int, x: int | float, result):
    if np.any(np.isnan(result)):
        assert np.isnan(main.coskx2(k, x)), (
            "Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.".format(
                result, main.coskx2(k, x)
            )
        )
    else:
        assert main.coskx2(k, x) == pytest.approx(result), (
            "Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.".format(
                result, main.coskx2(k, x)
            )
        )
