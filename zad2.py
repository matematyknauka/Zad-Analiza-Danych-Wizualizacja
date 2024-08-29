import pandas as pd
import zad2ModulFiltrowanieSelect as flt
df_csv = pd.read_csv('tabela.csv')['Produkt'].unique() # Wypisuje raz każdą wartośś z kolumny.

for produkt in df_csv:
    print(flt.filtr('tabela.csv', 'Produkt', produkt)) # Można do pliku w nowym katalogu zapisać.