import pandas as pd
import zad2ModulFiltrowanieSelect as flt
import shutil as sh
import os

directory = './tab_prod_csv' # Kropka oznacza obecny katalog roboczy.
stat = './stat_prod' # Obliczenia średnia,..., regresja dla każdego produktu
if os.path.exists(directory): # Sprawdzenie, czy katalog directory istnieje
  sh.rmtree(directory) # Jeśli istnieje to go usuwa.
os.makedirs(directory) # Tworzy pusty directory.

if os.path.exists(stat): # Sprawdzenie, czy katalog stat istnieje
  sh.rmtree(stat) # Jeśli istnieje to go usuwa.
os.makedirs(stat) # Tworzy pusty stat.

df_csv = pd.read_csv('tabela.csv')['Produkt'].unique() # Wypisuje raz każdą wartość z kolumny Produkt.

for produkt in df_csv: # Iteruje po produktach. Ewentualnie ich ID.
    flt.filtr('tabela.csv', 'Produkt', produkt).to_csv(directory + '/' + produkt + '.csv', index = False) # Dla każdego produktu robi tabelę. Czyli coś jak Select...
    read_prod = pd.read_csv(directory + '/' + produkt + '.csv') # Odczytuje plik dla iterowanego produktu.
    # print(read_prod['Sprzedaż'].mean())
    data_st = { # Dane statystyczne iterowanego produktu
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
    df_stat.to_csv(stat + '/Sta' + produkt + '.csv', index = False)

