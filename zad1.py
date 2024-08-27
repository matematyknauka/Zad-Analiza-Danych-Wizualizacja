import numpy as np
import pandas as pd

# Generowanie danych z brakującymi wartościami
data = {
    'Data': pd.to_datetime(['2024-08-01', '2024-08-02', '2024-08-03', None, '2024-08-05'] * 3),  # Brakująca data
    'Produkt': ['Produkt A'] * 5 + ['Produkt B'] * 5 + ['Produkt C'] * 5,
    'Kategoria': ['Kategoria 1'] * 4 + [None] + ['Kategoria 2'] * 5 + ['Kategoria 3'] * 5,  # Brakująca kategoria
    'Sprzedaż': [20, 30, 25, 15, None] * 3,  # Brakująca sprzedaż
    'Cena': [100, 200, None, 150, 250] * 3,  # Brakująca cena
}

# Tworzenie DataFrame
df = pd.DataFrame(data)

# Obliczanie zysku (z uwzględnieniem NaN)
df['Zysk'] = df['Sprzedaż'] * df['Cena']
# Normalizacja do zakresu [0, 1]
df['Normalizacja_Sprzedaż'] = (df['Sprzedaż'] - df['Sprzedaż'].min()) / (df['Sprzedaż'].max() - df['Sprzedaż'].min())
# Dane bez wierszy z brakującymi wartościami
# Alternatywnie można uzupełnić średnią brakujące dane. https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html
dfdr = df.dropna()
# Zapis do pliku CSV
dfdr.to_csv('tabela.csv', index=False)
# Odczyt z pliku tabela.csv
read = pd.read_csv('tabela.csv')
# print(read)