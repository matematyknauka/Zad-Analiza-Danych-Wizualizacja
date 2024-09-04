def run():
    import pandas as pd
    import zad2ModulFiltrowanieSelect as flt
    import shutil as sh
    import os

    directory = './tab_prod_csv' # Kropka oznacza obecny katalog roboczy.
    if os.path.exists(directory): # Sprawdzenie, czy katalog directory istnieje
      sh.rmtree(directory) # Jeśli istnieje to go usuwa.
    os.makedirs(directory) # Tworzy pusty directory.

    df_csv = pd.read_csv('tabela.csv')['Produkt'].unique() # Wypisuje raz każdą wartość z kolumny Produkt.

    for produkt in df_csv: # Iteruje po produktach. Ewentualnie ich ID.
        flt.filtr('tabela.csv', 'Produkt', produkt).to_csv(directory + '/' + produkt + '.csv') # Dla każdego produktu robi tabelę. Czyli coś jak Select...