def run():
    import pandas as pd
    import zad2ModulRegresja as reg
    import glob
    import os.path as osp

    for path in glob.glob('./tab_prod_csv/*'): # Iteracja po ścieżkach katalogu ./tab_prod_csv
        bsn = osp.basename(path) # Sama nazwa pliku bez ścieżki, np. foto.jpg. To tylko przykład pliku.
        spltx = osp.splitext(bsn)[0] # Krotka czyli coś podobnego do tablicy. 0 - nazwa, np. foto, 1 - rozszerzenie, np. jpg
        prod = pd.read_csv('./tab_prod_csv/' + spltx + '.csv') # np. Produkt A.csv Chyba można od razu prod = pd.read_csv('./tab_prod_csv/' + bsn)
        regr = reg.regresja(prod[['Cena']], prod[['Sprzedaż']]) # Z modułu zad2ModulRegresja
        print(regr)
