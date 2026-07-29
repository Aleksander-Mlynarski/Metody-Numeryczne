import numpy as np
import scipy
import math


def absolute_error(
    v: int | float | list | np.ndarray, v_approx: int | float | list | np.ndarray
) -> int | float | np.ndarray:
        
        try:
            v=np.asarray(v)
            v_approx=np.asarray(v_approx)
            err=np.abs(v-v_approx)
            return err
        except(ValueError,TypeError):
            return np.nan


def relative_error(
    v: int | float | list | np.ndarray, v_approx: int | float | list | np.ndarray
) -> int | float | np.ndarray:

        try:
            v=np.asarray(v)
            v_approx=np.asarray(v_approx)
            err=np.abs(v-v_approx)/v
            return err
        
        except(ValueError,TypeError):
            return np.nan



def p_diff(n: int, c: int | float) -> float:
    try:
        if not isinstance(n, int):
            return np.nan
        
        c_float = np.float64(c)
        b = np.float64(2**n)
        P1 = b - b + c_float
        P2 = b + c_float - b
        return abs(P1 - P2)
    
    except (TypeError, ValueError):
        return np.nan


def exponential(x: int | float, n: int) -> float:
    try:
        x=float(x)
        if n<0:
            return np.nan
        exp_approx=0
        for i in range(0,n):
            exp_approx+=(x**i)/math.factorial(i)
        return exp_approx
    
    except (TypeError, ValueError):
        return np.nan


def coskx1(k: int, x: int | float) -> float:
    try:
        if not isinstance(k, int) or k<0:
            return np.nan
        if k==0:
            return 1
        elif k==1:
            return np.cos(x)
        else:
            return 2*np.cos(x)*coskx1((k-1),x) - coskx1((k-2),x)
    except (TypeError, ValueError):
        return np.nan

def coskx2(k: int, x: int | float) -> tuple[float, float]:
    try:
        if not isinstance(k, int) or k<0:
            return np.nan
        k=abs(k)
        if k==0:
            return(1,0)
        elif k==1:
            return (np.cos(x),np.sin(x))
        else:
            (cos, sin) = coskx2(k-1, x) #tworzę funkcję coskx2, która zwróci krotkę (cos,sin)
            kcos = np.cos(x) * cos - np.sin(x) * sin #koncwoy wynik, który się rekurencyjnie oblicza
            ksin = np.sin(x) * cos + np.cos(x) * sin
            return (kcos, ksin)
    except (TypeError, ValueError):
        return np.nan

