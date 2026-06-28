# Metody Numeryczne

Zbiór laboratoriów z przedmiotu **Metody Numeryczne** (AGH). Repozytorium zawiera implementacje algorytmów numerycznych w Pythonie, testy jednostkowe oraz sprawozdania w formacie Jupyter Notebook.

**Autor:** Aleksander Młynarski

## O projekcie

Każde laboratorium to osobny moduł skupiony na innym zagadnieniu z analizy numerycznej — od podstaw Pythona i wizualizacji danych, przez algebrę liniową i równania nieliniowe, aż po całkowanie i równania różniczkowe. Kod jest weryfikowany automatycznymi testami (`pytest`), a wyniki i analizy opisane są w notebookach `sprawozdanie.ipynb`.

## Stos technologiczny

| Narzędzie | Zastosowanie |
|-----------|--------------|
| Python 3.11+ | implementacja algorytmów |
| NumPy | operacje macierzowe i wektorowe |
| SciPy | metody numeryczne (układy równań, całkowanie, EDO) |
| Matplotlib | wizualizacja wyników |
| pytest | testy jednostkowe |
| Jupyter | sprawozdania laboratoryjne |

## Struktura repozytorium

```
Metody Numeryczne/
├── lab1-python1-Aleksander-Mlynarski/     # Wstęp do Pythona
├── lab2-matplotlib-Aleksander-Mlynarski/  # Wizualizacja danych
├── lab3-Aleksander-Mlynarski/             # Błędy numeryczne
├── lab4-Aleksander-Mlynarski/             # Układy równań N×N
├── lab5-Aleksander-Mlynarski/             # Układy równań M×N
├── lab6-Aleksander-Mlynarski/             # Metody iteracyjne
├── lab7-Aleksander-Mlynarski/             # Pierwiastki wielomianów
├── lab8-Aleksander-Mlynarski/             # Równania nieliniowe
├── lab9-Aleksander-Mlynarski/             # Interpolacja
├── lab10-Aleksander-Mlynarski/            # Aproksymacja
├── lab11-Aleksander-Mlynarski/            # Całkowanie numeryczne
├── lab12-Aleksander-Mlynarski/            # Równania różniczkowe
├── requirements.txt
└── run_all_tests.py
```

W każdym katalogu laboratorium:

| Plik / folder | Opis |
|---------------|------|
| `main.py` | implementacja wymaganych funkcji |
| `test_main.py` | testy jednostkowe (dostarczone przez prowadzącego) |
| `sprawozdanie.ipynb` | sprawozdanie z analizą i wykresami |
| `expected/` | dane referencyjne do testów |

## Laboratoria

| Lab | Temat | Kluczowe algorytmy / koncepcje |
|-----|-------|--------------------------------|
| 1 | Wstęp do Pythona | funkcje, rekurencja, macierze NumPy |
| 2 | Matplotlib | wykresy, skale logarytmiczne, wizualizacja danych |
| 3 | Błędy numeryczne | błąd bezwzględny/względny, stabilność obliczeń |
| 4 | Układy równań N×N | macierze losowe, wartości osobliwe, residuum |
| 5 | Układy równań M×N | macierze rzadkie, układy prostokątne |
| 6 | Metody iteracyjne | dominacja diagonalna, GMRES / CG, residuum |
| 7 | Pierwiastki wielomianów | macierz Frobeniusa, wartości własne, `polyroots` |
| 8 | Równania nieliniowe | bisekcja, sieczna, Newton, iloraz różnicowy |
| 9 | Interpolacja | węzły Czebyszewa, interpolacja barycentryczna |
| 10 | Aproksymacja | metoda najmniejszych kwadratów |
| 11 | Całkowanie numeryczne | prostokątów, trapezów, całkowanie adaptacyjne |
| 12 | Równania różniczkowe | metoda Eulera, problem Arenstorfa |

## Uruchomienie

### Wymagania

```bash
python -m pip install -r requirements.txt
```

### Testy pojedynczego laboratorium

```bash
cd lab4-Aleksander-Mlynarski
python -m pytest test_main.py -v
```

### Testy wszystkich laboratoriów

```bash
python run_all_tests.py
```

### Sprawozdanie

Otwórz `sprawozdanie.ipynb` w wybranym katalogu laboratorium (Jupyter Lab, VS Code lub Jupyter Notebook).

## Co warto zobaczyć

- **lab4** — analiza uwarunkowania macierzy i wartości osobliwych
- **lab8** — implementacja klasycznych metod szukania pierwiastków od zera
- **lab9** — interpolacja barycentryczna na węzłach Czebyszewa
- **lab12** — numeryczne rozwiązywanie układów EDO (metoda Eulera, orbita Arenstorfa)
