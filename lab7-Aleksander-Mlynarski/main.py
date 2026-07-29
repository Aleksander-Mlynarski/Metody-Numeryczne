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
import numpy.polynomial.polynomial as nppoly


def roots_20(coef: np.ndarray) -> tuple[np.ndarray, np.ndarray] | None:
    """Funkcja wyznaczająca miejsca zerowe wielomianu funkcją
    `nppoly.polyroots()`, najpierw lekko zaburzając wejściowe współczynniki 
    wielomianu (N(0,1) * 1e-10).

    Args:
        coef (np.ndarray): Wektor współczynników wielomianu (n,).

    Returns:
        (tuple[np.ndarray, np. ndarray]):
            - Zaburzony wektor współczynników (n,),
            - Wektor miejsc zerowych (m,).
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    try:
        if np.ndim(coef)!=1:
            return None
        if not isinstance(coef, np.ndarray):
            return None
        coef_kopia= coef.astype(np.complex128) #pracujemy na kopii zeby nie modyfikowac oryginalui
        coef_kopia += np.random.random_sample(coef.shape)*1e-10
        roots_found = nppoly.polyroots(coef_kopia)
        return coef_kopia, roots_found

    except(ValueError,TypeError):
        return None


    """Funkcja służąca do wyznaczenia macierzy Frobeniusa na podstawie
    współczynników jej wielomianu charakterystycznego:
    w(x) = a_n*x^n + a_{n-1}*x^{n-1} + ... + a_2*x^2 + a_1*x + a_0

    Testy wymagają poniższej definicji macierzy Frobeniusa (implementacja dla 
    innych postaci nie jest zabroniona):
    F = [[       0,        1,        0,   ...,            0],
         [       0,        0,        1,   ...,            0],
         [       0,        0,        0,   ...,            0],
         [     ...,      ...,      ...,   ...,          ...],
         [-a_0/a_n, -a_1/a_n, -a_2/a_n,   ..., -a_{n-1}/a_n]]

    Args:
        coef (np.narray): Wektor współczynników wielomianu (n,).

    Returns:
        (np.ndarray): Macierz Frobeniusa o rozmiarze (n,n).
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
def frob_a(coef: np.ndarray) -> np.ndarray | None:
    try:
        if np.ndim(coef)!=1:
            return None
        if not isinstance(coef, np.ndarray):
            return None
        if coef.size < 2:
            return None
        
        n = coef.size - 1 
        a_n = coef[-1]
        if a_n == 0:
            return None
        frob_matrix = np.zeros((n, n))
        for i in range(n-1):
            frob_matrix[i, i + 1] = 1
        frob_matrix[-1, :] = -coef[:-1] / a_n
        return frob_matrix

    except(ValueError,TypeError):
        return None


    """Funkcja sprawdzająca czy podana macierz NIE JEST singularna. Przy
    implementacji należy pamiętać o definicji zera maszynowego.

    Args:
        A (np.ndarray): Macierz (n,n) do przetestowania.

    Returns:
        (bool): `True`, jeżeli macierz A nie jest singularna, w przeciwnym 
            wypadku `False`.
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
def is_nonsingular(A: np.ndarray) -> bool | None: 
    try:
        if not isinstance(A, np.ndarray) or A.ndim != 2 or A.shape[0] != A.shape[1]:
            return None
        det_A = np.linalg.det(A)
        eps_machine = np.finfo(float).eps
        if abs(det_A) > eps_machine:
            return True
        else:
            return False
    except(ValueError,TypeError):
            return None
