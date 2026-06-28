import numpy as np
import scipy
import math
def cylinder_area(r:float,h:float):
    
    if r<0 or h<0:
        return np.nan 
    pole = 2* math.pi * r**2 + 2*math.pi *r*h
    return pole
    """Obliczenie pola powierzchni walca. 
    Szczegółowy opis w zadaniu 1.
    
    Parameters:
    r (float): promień podstawy walca 
    h (float): wysokosć walca
    
    Returns:
    float: pole powierzchni walca 
    """
  

def fib(n:int):
    """Obliczenie pierwszych n wyrazów ciągu Fibonnaciego. 
    Szczegółowy opis w zadaniu 3.
    
    Parameters:
    n (int): liczba określająca ilość wyrazów ciągu do obliczenia 
    
    Returns:
    np.ndarray: wektor n pierwszych wyrazów ciągu Fibonnaciego.
    """

    
def fib(n: int):
    if not isinstance(n, int) or n < 0:
        return None
    if n == 0:
        return None
    if n == 1:
        return np.array([1])
    
    wynik = [1, 1]
    for i in range(2, n):
        wynik.append(wynik[i-1] + wynik[i-2])
    return np.array(wynik).reshape(1, -1)


def matrix_calculations(a:float):
    M = np.array([
            [a, 1, -a],
            [0, 1, 1],
            [-a, a, 1]
        ])
    Mdet = np.linalg.det(M)
    if Mdet ==0:
        Minv = np.nan
    else:
        Minv = np.linalg.inv(M)
    Mt = np.transpose(M)
    return (Minv, Mt, Mdet)
    """Funkcja zwraca wartości obliczeń na macierzy stworzonej 
    na podstawie parametru a.  
    Szczegółowy opis w zadaniu 4.
    
    Parameters:
    a (float): wartość liczbowa 
    
    Returns:
    touple: krotka zawierająca wyniki obliczeń 
    (Minv, Mt, Mdet) - opis parametrów w zadaniu 4.
    """
    return None

def custom_matrix(m:int, n:int):
    m = int(m)
    n = int(n)

    if (2 <= m <= 10) and (2 <= n <= 10):
        M = np.zeros( ( m, n ), dtype = int)
        for i in range(m):
            for j in range(n):
                if i > j:
                    M[i, j] = i
                else:
                    M[i, j] = j
        return M
