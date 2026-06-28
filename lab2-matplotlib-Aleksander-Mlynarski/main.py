import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import string
import random

def compare_plot(x1:np.ndarray,y1:np.ndarray,x2:np.ndarray,y2:np.ndarray,
                 xlabel: str,ylabel:str,title:str,label1:str,label2:str):
    """
    Funkcja do porównywania dwóch wykresów typu *plot*.  
    Szczegółowy opis znajduje się w zadaniu 3.

    Parameters
    ----------
    x1 : np.ndarray  
        Wektor wartości osi X dla pierwszego wykresu.  
    y1 : np.ndarray  
        Wektor wartości osi Y dla pierwszego wykresu.  
    x2 : np.ndarray  
        Wektor wartości osi X dla drugiego wykresu.  
    y2 : np.ndarray  
        Wektor wartości osi Y dla drugiego wykresu.  
    xlabel : str  
        Etykieta osi X.  
    ylabel : str  
        Etykieta osi Y.  
    title : str  
        Tytuł wykresu.  
    label1 : str  
        Opis serii danych z pierwszego wykresu (legenda).  
    label2 : str  
        Opis serii danych z drugiego wykresu (legenda).  

    Returns
    -------
    matplotlib.pyplot.figure  
        Wykres porównujący dane (x1, y1) i (x2, y2), zgodny z opisem z zadania 4.  
    """


    if x1.shape != y1.shape or x2.shape != y2.shape  or  min(x1.shape)==0 or min(x2.shape)==0:
        return None
    fig, ax = plt.subplots()
    ax.plot(x1, y1, color='blue', linewidth=4, label=label1)
    ax.plot(x2, y2, color='red', linewidth=2, label=label2)
    ax.set(xlabel=xlabel, ylabel=ylabel, title=title)
    ax.legend()
    ax.grid(True)
    
    return fig



def parallel_plot(x1:np.ndarray,y1:np.ndarray,x2:np.ndarray,y2:np.ndarray,
                  x1label:str,y1label:str,x2label:str,y2label:str,title:str,orientation:str):
    if x1.size == 0 or y1.size == 0 or x2.size == 0 or y2.size == 0:
        return None
    if len(x1) != len(y1) or len(x2) != len(y2):
        return None
    if orientation == '-':
        rows, cols = 1, 2
    elif orientation == '|':
        rows, cols = 2, 1
    else:
        return None
    fig, axes = plt.subplots(rows, cols)
    axes[0].plot(x1, y1, color='blue')
    axes[0].set_xlabel(x1label)
    axes[0].set_ylabel(y1label)
    axes[0].grid(True)

    axes[1].plot(x2, y2, color='red')
    axes[1].set_xlabel(x2label)
    axes[1].set_ylabel(y2label)
    axes[1].grid(True)
    return fig
    """
    Funkcja do tworzenia dwóch wykresów typu *plot* w układzie subplot.  
    Wykresy mogą być ustawione pionowo lub poziomo.  
    Szczegółowy opis znajduje się w zadaniu 5.

    Parameters
    ----------
    x1 : np.ndarray  
        Wektor wartości osi X dla pierwszego wykresu.  
    y1 : np.ndarray  
        Wektor wartości osi Y dla pierwszego wykresu.  
    x2 : np.ndarray  
        Wektor wartości osi X dla drugiego wykresu.  
    y2 : np.ndarray  
        Wektor wartości osi Y dla drugiego wykresu.  
    x1label : str  
        Etykieta osi X dla pierwszego wykresu.  
    y1label : str  
        Etykieta osi Y dla pierwszego wykresu.  
    x2label : str  
        Etykieta osi X dla drugiego wykresu.  
    y2label : str  
        Etykieta osi Y dla drugiego wykresu.  
    title : str  
        Tytuł całej figury.  
    orientation : str  
        Określa układ subplotów:  
        - `'-'` → dwa wiersze (układ pionowy),  
        - `'|'` → dwie kolumny (układ poziomy).  

    Returns
    -------
    matplotlib.pyplot.figure  
        Figura z dwoma wykresami (x1, y1) i (x2, y2), zgodna z opisem z zadania 5.  
    """




    """
    Funkcja do tworzenia wykresów z zastosowaniem skali logarytmicznej.  
    Szczegółowy opis znajduje się w zadaniu 7.

    Parameters
    ----------
    x : np.ndarray  
        Wektor wartości osi X.  
    y : np.ndarray  
        Wektor wartości osi Y.  
    xlabel : str  
        Etykieta osi X.  
    ylabel : str  
        Etykieta osi Y.  
    title : str  
        Tytuł wykresu.  
    log_axis : str  
        Określa, na której osi zastosować skalę logarytmiczną:  
        - `'x'`  → logarytmiczna skala osi X,  
        - `'y'`  → logarytmiczna skala osi Y,  
        - `'xy'` → logarytmiczna skala na obu osiach.  

    Returns
    -------
    matplotlib.pyplot.figure  
        Wykres (x, y) ze skalą logarytmiczną, zgodny z opisem z zadania 7.  
    """
def log_plot(x:np.ndarray,y:np.ndarray,xlabel:np.ndarray,ylabel:str,title:str,log_axis:str):
    if x.size != y.size:
        return None
    fig, ax = plt.subplots()
    ax.plot(x,y)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    if log_axis == 'x':
        ax.set_xscale('log')
    elif log_axis == 'y':
        ax.set_yscale('log')
    elif log_axis == 'xy':
        ax.set_xscale('log')
        ax.set_yscale('log')



