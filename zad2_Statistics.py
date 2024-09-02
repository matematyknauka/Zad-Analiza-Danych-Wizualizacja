import os
import shutil as sh
import glob
import pandas as pd

stat = './stat_prod' # Obliczenia średnia,..., regresja dla każdego produktu
if os.path.exists(stat): # Sprawdzenie, czy katalog stat istnieje
  sh.rmtree(stat) # Jeśli istnieje to go usuwa.
os.makedirs(stat) # Tworzy pusty stat.

for file_csv_path in glob.glob('./tab_prod_csv/*'):
    f_csv = os.path.basename(file_csv_path)
    prod = os.path.splitext(f_csv)[0]
    # print(prod)
    read_prod = pd.read_csv('./tab_prod_csv/' + prod + '.csv')
    data_st = { # Dane statystyczne konkretnego produktu (iterowanie)
      'Średnia (Sprzedaż)': [read_prod['Sprzedaż'].mean()],
      'Odchylenie (Sprzedaż)' : [read_prod['Sprzedaż'].std()],
      'Mediana (Sprzedaż)' : [read_prod['Sprzedaż'].median()],
      'Moda (Sprzedaż)' : [read_prod['Sprzedaż'].mode()[0]], # Moda ta najmniejsza bo może być wiele wartości, które występują najczęściej, np. 5, 5, 2, 2.

      'Średnia (Zysk)': [read_prod['Zysk'].mean()],
      'Odchylenie (Zysk)' : [read_prod['Zysk'].std()],
      'Mediana (Zysk)' : [read_prod['Zysk'].median()],
      'Moda (Zysk)' : [read_prod['Zysk'].mode()[0]]
    }
    df_stat = pd.DataFrame(data_st)
    df_stat.to_csv(stat + '/stat' + prod + '.csv')

