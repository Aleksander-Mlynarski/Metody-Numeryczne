# =================================  TESTY  ===================================
# Testy do tego pliku obejmują jedynie weryfikację poprawności wyników dla
# prawidłowych danych wejściowych - obsługa niepoprawych danych wejściowych
# nie jest ani wymagana ani sprawdzana. W razie potrzeby lub chęci można ją
# wykonać w dowolny sposób we własnym zakresie.
# =============================================================================
import numpy as np
from typing import Callable


def solve_euler(
    func: Callable[[float, np.ndarray], np.ndarray],
    t_span: np.ndarray,
    y0: np.ndarray,
) -> np.ndarray | None:
    """Funkcja rozwiązująca układ równań różniczkowych metodą Eulera w przód.

    Args:
        func (Callable[[float, np.ndarray], np.ndarray]): Prawa strona równania
            w postaci fun(t, y), gdzie `t` to skalar, a `y` to wektor (n,)
            lub (n,k). Funkcja musi zwracać wektor o takim samym kształcie
            jak `y`.
        t_span (np.ndarray): Wektor czasu (m,), dla którego ma zostać
            znalezione rozwiązanie.
        y0 (np.ndarray): Warunek początkowy w postaci wektora (n,).

    Returns:
        (np.ndarray): Macierz o wymiarze (n,m) zawierająca rozwiązania
        w kolejnych punktach czasowych.
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    try:
        
        if not isinstance(t_span, np.ndarray) or not isinstance(y0, np.ndarray):
            return None
        if t_span.ndim != 1:
            return None
        if y0.ndim != 1:
            return None
        if t_span.size < 2:
            return None

        n = y0.shape[0]
        m = t_span.shape[0]
        y = np.zeros((n, m), dtype=float)
        y[:, 0] = y0

        for i in range(1, m):
            dt = t_span[i] - t_span[i - 1]
            f_val = func(t_span[i - 1], y[:, i - 1])
            if f_val is None or f_val.shape != (n,):
                return None
            y[:, i] = y[:, i - 1] + dt * f_val

        return y
    except Exception:
        return None


def arenstorf(t: float, x: np.ndarray) -> np.ndarray | None:
    """Funkcja definiująca układ równań różniczkowych opisujących orbitę 
    Arenstorfa.

    Args:
        t (float): Chwila czasu (tu nieużywane, ale wymagane przez solvery).
        x (np.ndarray): Wektor stanu postaci: (x_pos, x_vel, y_pos, y_vel).

    Returns:
        (np.ndarray): Wektor pochodnych stanu: (x_vel, x_acc, y_vel, y_acc).
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    try:
        if not isinstance(x, np.ndarray):
            return None
        if x.shape != (4,):
            return None

        mu = 0.012277471
        mu_p = 1.0 - mu   # μ′

        x_pos = x[0]
        x_vel = x[1]
        y_pos = x[2]
        y_vel = x[3]

        D1 = ((x_pos + mu)**2 + y_pos**2)**(3/2)
        D2 = ((x_pos - mu_p)**2 + y_pos**2)**(3/2)

        if D1 == 0 or D2 == 0:
            return None

        dx1 = x_vel
        dx2 = x_pos + 2*y_vel - mu_p*(x_pos + mu)/D1 - mu*(x_pos - mu_p)/D2
        dx3 = y_vel
        dx4 = y_pos - 2*x_vel - mu_p*y_pos/D1 - mu*y_pos/D2
        return np.array([dx1, dx2, dx3, dx4], dtype=float)

    except Exception:
        return None