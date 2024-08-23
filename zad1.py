import numpy as np
import pandas as pd

data = {'Data':[pd.NaT, '24/08/20', '23/10/13', '22/11/07', '88/11/15'], 'Produkt':['Produkt A', 'Produkt B', 'Produkt C', 'Produkt D', 'Produkt E'], 'Kategoria':['Kategoria 1', 'Kategoria 2', np.nan, 'Kategoria 4', 'Kategoria 5'], 'Sprzedaż':[20, 5, 30, 50, np.nan], 'Cena':[100, 300, 500, 100.5, 300], 'Zysk':[0, 0, 0, 0, 0]}
df_bw = pd.DataFrame(data) # Tabela z brakującymi wartościami
df = pd.DataFrame(data).dropna() # dropna() usuwa wiersze z pustymi wartościami.
df['Data'] = pd.to_datetime(df['Data'], format='%y/%m/%d')
df['Zysk'] = df['Sprzedaż'] * df['Cena']
print("Tabela po usunięciu pustych wartości (metoda dropna()), która nie jest z pliku:\n")
print(df.to_string(index=False))
df.to_csv('tabela.csv', index = False)
read = pd.read_csv('tabela.csv')
print("\nTabela z pliku tabela.csv\n")
print(read.to_string(index = False))
print("\nTabela bez usuniętych pustych wartości:\n")
print(df_bw)
isn = df_bw.isnull()
print("\nMetoda isnull() - wypisuje true jeśli brak wartości, w przeciwnym przypadku false.\n")
print(isn)