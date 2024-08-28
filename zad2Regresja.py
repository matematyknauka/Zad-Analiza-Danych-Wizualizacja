# Regresja liniowa dla zależności sprzedaży (ilości sprzedanego towaru) od ceny
# !!! Przefiltrować dla konkretnego towaru
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd

df_SC = pd.read_csv('tabela.csv')[['Cena', 'Sprzedaż']]

# Przygotowanie danych
X = df_SC[['Cena']].values  # Zmienna niezależna
y = df_SC['Sprzedaż'].values     # Zmienna zależna

# Tworzenie modelu regresji
model = LinearRegression()
model.fit(X, y)

# Współczynniki
slope = model.coef_[0]  # Współczynnik kierunkowy
intercept = model.intercept_  # Wyraz wolny

print(f'Współczynnik kierunkowy: {slope}')
print(f'Wyraz wolny: {intercept}')