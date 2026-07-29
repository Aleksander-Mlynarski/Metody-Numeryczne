# =================================  TESTY  ===================================
# Testy do tego pliku obejmują jedynie weryfikację poprawności wyników dla
# prawidłowych danych wejściowych - obsługa niepoprawych danych wejściowych
# nie jest ani wymagana ani sprawdzana. W razie potrzeby lub chęci można ją
# wykonać w dowolny sposób we własnym zakresie.
# =============================================================================
import numpy as np


def linear_least_squares(x: np.ndarray, y: np.ndarray) -> np.ndarray | None:
    """Funkcja obliczająca współczynniki liniowej aproksymacji metodą
    najmniejszych kwadratów.

    Args:
        y (np.ndarray): Wektor wartości y punktu danych (n,).
        x (np.ndarray): Wektor wartości x punktu danych (n,).

    Returns:
        (np.ndarray): Wektor współczynników aproksymacji.
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    
    try:
        if x.ndim != 1 or y.ndim != 1 or x.shape[0] != y.shape[0]:
            return None
        n = x.shape[0]
        x_mean = np.mean(x)
        y_mean = np.mean(y)

        Sxy = np.sum((x - x_mean) * (y - y_mean))
        Sxx = np.sum((x - x_mean) ** 2)

        if Sxx == 0:
            return None

        a = Sxy / Sxx
        b = y_mean - a * x_mean

        return np.array([a, b])
    except(ValueError,TypeError):
        return None

linear_least_squares(np.array([2,3,4,5,7,9]),np.array([4.87,6.36,8.1,10.92,14.39,18.88]))
def chebyshev_nodes(
    n: int, interval: tuple[float, float] = (-1., 1.)
) -> np.ndarray | None:
    """Funkcja generująca wektor węzłów Czebyszewa pierwszego rodzaju (n,)
    dla zadanego przedziału i sortująca wynik od najmniejszego do największego
    węzła.

    Args:
        n (int): Liczba węzłów Czebyszewa.
        interval (tuple[float, float]): Przedział, na którym mają być
            wygenerowane węzły (początek, koniec).

    Returns:
        (np.ndarray): Posortowany wektor węzłów Czebyszewa (n,).
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    try:
        if n <= 0 or not isinstance(interval, tuple) or len(interval) != 2:
            return None
        if not isinstance(n, int) or n <= 0:
            return None
        a, b = interval
        if a == b:
            return None
        if a > b:
            a, b = b, a
        

        k = np.arange(1, n + 1)
        nodes = 0.5 * (a + b) + 0.5 * (b - a) * np.cos((2 * k - 1) * np.pi / (2 * n))
        return np.sort(nodes)
    except(ValueError,TypeError):
        return None
    
