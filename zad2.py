import pandas as pd
import zad2ModulFiltrowanieSelect as flt
import shutil as sh
import os

directory = './tab_prod_csv'
if os.path.exists(directory):
  sh.rmtree(directory)
os.makedirs(directory)

df_csv = pd.read_csv('tabela.csv')['Produkt'].unique() # Wypisuje raz każdą wartośś z kolumny.

for produkt in df_csv:
    flt.filtr('tabela.csv', 'Produkt', produkt).to_csv(directory + '/' + produkt + '.csv')