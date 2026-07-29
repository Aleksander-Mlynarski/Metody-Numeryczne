# =================================  TESTY  ===================================
# Testy do tego pliku obejmują jedynie weryfikację poprawności wyników dla
# prawidłowych danych wejściowych - obsługa niepoprawych danych wejściowych
# nie jest ani wymagana ani sprawdzana. W razie potrzeby lub chęci można ją 
# wykonać w dowolny sposób we własnym zakresie.
# =============================================================================
import numpy as np


def chebyshev_nodes(n: int = 18) -> np.ndarray | None:
    """Funkcja generująca wektor węzłów Czebyszewa drugiego rodzaju (n,) 
    i sortująca wynik od najmniejszego do największego węzła.

    Args:
        n (int): Liczba węzłów Czebyszewa.
    
    Returns:
        (np.ndarray): Wektor węzłów Czebyszewa (n,).
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    if not isinstance(n, int) or n < 1:
        return None

    nodes = np.array([np.cos(k * np.pi /(n-1)) for k in range(n)])
    return nodes 
chebyshev_nodes(18)

def bar_cheb_weights(n: int = 10) -> np.ndarray | None:
    """Funkcja tworząca wektor wag dla węzłów Czebyszewa wymiaru (n,).

    Args:
        n (int): Liczba wag węzłów Czebyszewa.
    
    Returns:
        (np.ndarray): Wektor wag dla węzłów Czebyszewa (n,).
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    if not isinstance(n, int) or n < 2:
        return None
    w_i=[np.power(-1,i) for i in range(n)]
    w_i[0]=0.5
    w_i[n-1]=0.5*(-1)**(n-1)
    return np.array(w_i)


def barycentric_inte(
    xi: np.ndarray, yi: np.ndarray, wi: np.ndarray, x: np.ndarray
) -> np.ndarray | None:
    """Funkcja przeprowadza interpolację metodą barycentryczną dla zadanych 
    węzłów xi i wartości funkcji interpolowanej yi używając wag wi. Zwraca 
    wyliczone wartości funkcji interpolującej dla argumentów x w postaci 
    wektora (n,).

    Args:
        xi (np.ndarray): Wektor węzłów interpolacji (m,).
        yi (np.ndarray): Wektor wartości funkcji interpolowanej w węzłach (m,).
        wi (np.ndarray): Wektor wag interpolacji (m,).
        x (np.ndarray): Wektor argumentów dla funkcji interpolującej (n,).
    
    Returns:
        (np.ndarray): Wektor wartości funkcji interpolującej (n,).
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    try:
        xi_arr = np.array(xi)
        yi_arr = np.array(yi)
        wi_arr = np.array(wi)
        x_arr = np.array(x)

        if not (xi_arr.ndim == yi_arr.ndim == wi_arr.ndim == 1):
            return None
        if not (xi_arr.shape == yi_arr.shape == wi_arr.shape):
            return None
        licz = np.zeros_like(x_arr, dtype=float)
        mian = np.zeros_like(x_arr, dtype=float)
  
        for i in range(len(x_arr)):
            for j in range(len(xi_arr)):
                if x_arr[i] == xi_arr[j]:
                    licz[i] = yi_arr[j]
                    mian[i] = 1.0
                    break
            else:
                for j in range(len(xi_arr)):
                    diff = x_arr[i] - xi_arr[j]
                    temp = wi_arr[j] / diff
                    licz[i] += temp * yi_arr[j]
                    mian[i] += temp

                continue 
            continue

        return licz / mian
    
    except Exception:
        return None



def L_inf(
    xr: int | float | list | np.ndarray, x: int | float | list | np.ndarray
) -> float | None:
    """Funkcja obliczająca normę L-nieskończoność. Powinna działać zarówno na 
    wartościach skalarnych, listach, jak i wektorach biblioteki numpy.

    Args:
        xr (int | float | list | np.ndarray): Wartość dokładna w postaci 
            skalara, listy lub wektora (n,).
        x (int | float | list | np.ndarray): Wartość przybliżona w postaci 
            skalara, listy lub wektora (n,).

    Returns:
        (float): Wartość normy L-nieskończoność.
        Jeżeli dane wejściowe są niepoprawne funkcja zwraca `None`.
    """
    try:
        xr_arr = np.array(xr)
        x_arr = np.array(x)

        if xr_arr.shape != x_arr.shape:
            return None
        
        diff = np.abs(xr_arr - x_arr)
        
        return float(np.max(diff))

    except Exception:
        return None
