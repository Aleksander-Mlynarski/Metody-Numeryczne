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
import scipy as sp


def is_diagonally_dominant(A: np.ndarray | sp.sparse.csc_array) -> bool | None:
    """Funkcja sprawdzająca czy podana macierz jest diagonalnie zdominowana.

    Args:
        A (np.ndarray | sp.sparse.csc_array): Macierz A (m,m) podlegająca 
            weryfikacji.
    
    Returns:
        (bool): `True`, jeśli macierz jest diagonalnie zdominowana, 
            w przeciwnym wypadku `False`.
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    try:
        if not isinstance(A, (np.ndarray, sp.sparse.csc_array)):
            return None
        if A.ndim != 2 or A.shape[0] != A.shape[1]:
            return None
        
        if isinstance(A, sp.sparse.csc_array):
            A = A.toarray()

        A_abs = np.abs(A)
        diag_abs = np.diagonal(A_abs) 
        diag_sums = np.sum(A_abs, axis=1)
        return np.all(diag_abs >= diag_sums)

    except(ValueError, TypeError, AttributeError):
        return None



def residual_norm(A: np.ndarray, x: np.ndarray, b: np.ndarray) -> float | None:
    """Funkcja obliczająca normę residuum dla równania postaci: 
    Ax = b.

    Args:
        A (np.ndarray): Macierz A (m,n) zawierająca współczynniki równania.
        x (np.ndarray): Wektor x (n,) zawierający rozwiązania równania.
        b (np.ndarray): Wektor b (m,) zawierający współczynniki po prawej 
            stronie równania.
    
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
