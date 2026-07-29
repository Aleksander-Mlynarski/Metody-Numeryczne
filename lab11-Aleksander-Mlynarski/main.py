# =================================  TESTY  ===================================
# Testy do tego pliku obejmują jedynie weryfikację poprawności wyników dla
# prawidłowych danych wejściowych - obsługa niepoprawych danych wejściowych
# nie jest ani wymagana ani sprawdzana. W razie potrzeby lub chęci można ją 
# wykonać w dowolny sposób we własnym zakresie.
# =============================================================================
import numpy as np
from typing import Callable


def rectangular_rule(
    func: Callable[[float], float], a: float, b: float, n: int
) -> float | None:
    """Oblicza przybliżoną wartość całki oznaczonej metodą prostokątów.

    Args:
        func (Callable[[float], float]): Funkcja, której całka ma być 
            obliczona.
        a (float): Dolna granica całkowania.
        b (float): Górna granica całkowania.
        n (int): Liczba podprzedziałów (większa liczba daje dokładniejsze 
            przybliżenie).
    
    Returns:
        (float): Przybliżona wartość całki oznaczonej.
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    try:
        if n <= 0 or a >= b:
            return None
        if not callable(func):
            return None

        delta_x = (b - a) / n
        integral = 0.0

        for i in range(n):
            x_i = a + i * delta_x
            integral += func(x_i)

        return integral * delta_x
    except Exception:
        return None

def trapezoidal_rule(
    func: Callable[[float], float], a: float, b: float, n: int
) -> float | None:
    """Oblicza przybliżoną wartość całki oznaczonej metodą trapezów.

    Args:
        func (Callable[[float], float]): Funkcja, której całka ma być 
            obliczona.
        a (float): Dolna granica całkowania.
        b (float): Górna granica całkowania.
        n (int): Liczba podprzedziałów (większa liczba daje dokładniejsze 
            przybliżenie).
    
    Returns:
        (float): Przybliżona wartość całki oznaczonej.
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    try:
        if not isinstance(n, int) or n <= 0 or a >= b:
            return None
        if not callable(func):
            return None
        delta_x = (b - a) / n
        integral = 0.5 * (func(a) + func(b))
        for i in range(1, n):
            x_i = a + i * delta_x
            integral += func(x_i)
        return integral * delta_x
    except Exception:
        return None    


def custom_integration(
    func: Callable[[float], float], a: float, b: float, order: int
) -> float | None:
    """Oblicza przybliżoną wartość całki oznaczonej za pomocą kwadratury 
    Gaussa-Legendre'a.

    Args:
        func (Callable[[float], float]): Funkcja, której całka ma być 
            obliczona.
        a (float): Dolna granica całkowania.
        b (float): Górna granica całkowania.
        order (int): Rząd kwadratury Gaussa-Legendre'a.
    
    Returns:
        (float): Przybliżona wartość całki oznaczonej.
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    pass
