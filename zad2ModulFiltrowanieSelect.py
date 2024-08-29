def filtr(plik, kolumna, wartosc):
    import pandas as pd

    df = pd.read_csv(plik)
    tabela = df[df[kolumna] == wartosc]
    return tabela

# Przykład użycia w pliku z projektu:
# import zad2ModulFiltrowanieSelect as mf

#  print(mf.filtr('tabela.csv', 'Produkt', 'Produkt C')[['Cena', 'Sprzedaż']])