# Laboratorium 12
## Równania różniczkowe zwyczajne

Numeryczne rozwiązywanie układów równań różniczkowych metodą Eulera w przód. Implementacja obejmuje solver EDO oraz model problemu Arenstorfa (orbita okresowa w układzie ciał ciężkich).

## Pliki

| Plik | Opis |
|------|------|
| `main.py` | `solve_euler()` — metoda Eulera; `arenstorf()` — prawa strona układu Arenstorfa |
| `test_main.py` | testy jednostkowe |
| `sprawozdanie.ipynb` | sprawozdanie z analizą dokładności i wizualizacją orbity |

## Uruchomienie testów

```bash
python -m pytest test_main.py -v
```

## Podstawowe informacje

1. Wszystkie niezbędne pliki do wykonania ćwiczenia znajdują się w repozytorium. Nie należy usuwać żadnych plików.
2. **Nie należy edytować pliku test_main.py**. Zmiana testów spowoduje brak zaliczenia danego laboratorium.
3. Zaliczenie testów nie oznacza ukończenia danego laboratorium, należy również uzupełnić plik sprawozdanie.ipynb
4. Sprawozdania oraz kod muszą być wykonane samodzielnie, w razie wykrycia plagiatów zostaną wszczęte kroki zgodne z Regulaminem Studiów AGH
5. Można tworzyć pomocnicze moduły/skrypty/klasy według uznania, kod musi jedynie przechodzić testy na serwerze CI.
6. Środowisko programistyczne do laboratorium jest sprawą indywidualną studenta, rekomendowany jest edytor VS Code.
7. W razie jakichkolwiek niejasności należy skontaktować się z prowadzącym zajęcia.

## Materiały uzupełniające

- [Scipy Lecture Notes](http://www.scipy-lectures.org/index.html)
- [NumPy](https://www.numpy.org)
- [SciPy — rozwiązywanie EDO](https://docs.scipy.org/doc/scipy/tutorial/integrate.html)
- [Matplotlib](https://matplotlib.org/)
