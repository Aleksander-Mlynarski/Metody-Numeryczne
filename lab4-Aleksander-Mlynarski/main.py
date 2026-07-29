import numpy as np
import pickle

from typing import Union, List, Tuple
#z tablicy z lekcji:
#np.ndarray([v1,v2]) wektor (2,)
#np.ndarray([[v1,v2]]) macierz (1,2)
#np.ndarray([[v1],[v2]]) macierz (2,1)
def random_matrix_Ab(m:int):
    try:
        if not isinstance(m, int):
             return None
        A=np.random.randint(1,10,size=(m,m))
        b=np.random.randint(1,10, size=(m))
        return A,b
    except(ValueError,TypeError):
            return None
def residual_norm(A:np.ndarray,x:np.ndarray, b:np.ndarray):
    try:
        c=np.dot(A,x)
        r= b- c
        return np.linalg.norm(r)
    except(ValueError,TypeError):
            return None
    
def log_sing_value(n:int, min_order:Union[int,float], max_order:Union[int,float]):

    try:
        if n<=0 or not isinstance(n,int) or not isinstance(max_order,[int,float]) or not isinstance(min_order,[int,float]):
             return None
        wartosci = np.logspace(start=max_order, stop=min_order, num=n, base=10.0)
        return wartosci
    except(ValueError,TypeError):
        return None

    
def order_sing_value(n:int, order:Union[int,float] = 2, site:str = 'gre'):
    try:
        n = int(n) #Należało tutaj n i order tak skonwertować i usunąć warunek ze "not isistance", ponieważ testy chciały jakby wynik dla tych wartości, a nie None.
        order = float(order)

        zmiana = 10**order
        wartosci = np.random.rand(n)*10
        wartosci = np.sort(wartosci)[::-1] #odwraca kolejność
        if site == 'low':
            wartosci[-1] = wartosci[-1] *zmiana
        elif site == 'gre':
            wartosci[0] = wartosci[0] * zmiana
        else:
            return None
        wartosci = np.sort(wartosci)[::-1] #ponowne sortowanie
        return wartosci

    except(ValueError,TypeError):
        return None


def create_matrix_from_A(A:np.ndarray, sing_value:np.ndarray):
    try:
        U, s, V = np.linalg.svd(A)
        if s.shape != sing_value.shape:
            return None
        A1 = np.dot(U * sing_value, V)
        return A1

    except(ValueError,TypeError, AttributeError): #dodałem AttribiuteError, ponieważ był taki błąd w testach
        return None