# =================================  TESTY  ===================================
# Testy do tego pliku zostały podzielone na dwie kategorie:
#
#  1. `..._invalid_input`:
#     - Sprawdzające poprawną obsługę nieprawidłowych danych wejściowych.
#
#  2. `..._correct_solution`:
#     - Weryfikujące poprawność wyników dla prawidłowych danych wejściowych.
# =============================================================================
import numpy as np
#A.ndim
#len(A.shape)
#A.shape==(b.shape[0],x.shape[0])

def spare_matrix_Abt(m: int, n: int) -> tuple[np.ndarray, np.ndarray] | None:
    """Funkcja tworząca zestaw składający się z macierzy A (m,n) i
    wektora b (m,) na podstawie pomocniczego wektora t (m,).

    Args:
        m (int): Liczba wierszy macierzy A.
        n (int): Liczba kolumn macierzy A.

    Returns:
        (tuple[np.ndarray, np.ndarray]):
            - Macierz A o rozmiarze (m,n),
            - Wektor b (m,).
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    try:
        if not isinstance(m, int) or not isinstance(n,int) or m<1 or n<1:
             return None
        t=np.linspace(0,1,m)
        A=np.vander(t,N=n,increasing=True)
        b=np.cos(4*t)
        return A,b
    except(ValueError,TypeError, AttributeError):
        return None

def square_from_rectan(
    A: np.ndarray, b: np.ndarray
) -> tuple[np.ndarray, np.ndarray] | None:
    """Funkcja przekształcająca układ równań z prostokątną macierzą współczynników
    na kwadratowy układ równań.
    A^T * A * x = A^T * b  ->  A_new * x = b_new

    Args:
        A (np.ndarray): Macierz A (m,n) zawierająca współczynniki równania.
        b (np.ndarray): Wektor b (m,) zawierający współczynniki po prawej stronie równania.

    Returns:
        (tuple[np.ndarray, np.ndarray]):
            - Macierz A_new o rozmiarze (n,n),
            - Wektor b_new (n,).
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    try:
        if not isinstance(A, np.ndarray) or not isinstance(b,np.ndarray):
             return None
        if A.ndim != 2 or b.ndim != 1:
            return None
        if A.shape[0] != b.shape[0]:
            return None
        A_transponowane = np.transpose(A)
        A_new = np.dot(A_transponowane, A)
        b_new = np.dot(A_transponowane, b)
        return A_new,b_new
    except(ValueError, TypeError, AttributeError):
        return None

def residual_norm(A: np.ndarray, x: np.ndarray, b: np.ndarray) -> float | None:
    """Funkcja obliczająca normę residuum dla równania postaci:
    Ax = b

    Args:
        A (np.ndarray): Macierz A (m,n) zawierająca współczynniki równania.
        x (np.ndarray): Wektor x (n,) zawierający rozwiązania równania.
        b (np.ndarray): Wektor b (m,) zawierający współczynniki po prawej stronie równania.

    Returns:
        (float): Wartość normy residuum dla podanych parametrów.
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    try:
        if not isinstance(A, np.ndarray) or not isinstance(b,np.ndarray) or not isinstance(x,np.ndarray):
             return None
        if(not A.ndim ==2 or not b.ndim==1 or not x.ndim==1):
            return None
        if (
            A.shape[0] != b.shape[0] or
            A.shape[1] !=x.shape[0]):
            return None
        c= A@x
        r=b- c
        residual_norm= np.linalg.norm(r)
        return residual_norm
    except(ValueError, TypeError, AttributeError):
        return None

