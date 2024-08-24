import numpy as np
import pandas as pd

data = {'Data':[pd.NaT, '24/08/20', '23/10/13', '22/11/07', '88/11/15'], 'Produkt':['Produkt A', 'Produkt B', 'Produkt C', 'Produkt D', 'Produkt E'], 'Kategoria':['Kategoria 1', 'Kategoria 2', np.nan, 'Kategoria 4', 'Kategoria 5'], 'Sprzedaż':[20, 5, 30, 50, np.nan], 'Cena':[100, 300, 500, 100.5, 300], 'Zysk':[0, 0, 0, 0, 0], 'Normalizacja_Sprzedaż':[0, 0, 0, 0, 0]}
df = pd.DataFrame(data)
df['Zysk'] = df['Sprzedaż'] * df['Cena']
df['Normalizacja_Sprzedaż'] = (df['Sprzedaż'] - df['Sprzedaż'].min()) / (df['Sprzedaż'].max() - df['Sprzedaż'].min())
dfdr = df.dropna() # Alternatywnie można uzupełnić średnią brakujące dane. https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html
dfdr.to_csv('tabela.csv', index = False)
read = pd.read_csv('tabela.csv')
print(read)