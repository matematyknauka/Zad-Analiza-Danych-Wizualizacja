def regresja(kolumna_x, kolumna_y): # kolumny z tabeli
    # Regresja liniowa dla zależności wartości od argumentu (dla kolumny)
    from sklearn.linear_model import LinearRegression
    import numpy as np
    import pandas as pd

    # Przygotowanie danych
    X = kolumna_x.values  # Zmienna niezależna
    y = kolumna_y.squeeze().values     # Zmienna zależna. squeeze bo chodzi o serie.

    # Tworzenie modelu regresji
    model = LinearRegression()
    model.fit(X, y)

    # Współczynniki
    slope = model.coef_[0]  # Współczynnik kierunkowy
    intercept = model.intercept_  # Wyraz wolny

    return [slope, intercept]