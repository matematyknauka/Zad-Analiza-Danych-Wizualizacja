import pandas as pd

data = {'Data':['24/08/20', '23/10/13', '22/11/07'], 'Produkt':['Produkt A', 'Produkt B', 'Produkt C'], 'Kategoria':['Kategoria 1', 'Kategoria 2', 'Kategoria 3'], 'Sprzedaż':[20, 5, 30], 'Cena':[100, 300, 500], 'Zysk':[0, 0, 0]}
df = pd.DataFrame(data)
df['Data'] = pd.to_datetime(df['Data'], format='%y/%m/%d')
df['Zysk'] = df['Sprzedaż'] * df['Cena']
# print(df.to_string(index=False))
df.to_csv('tabela.csv', index = False)
read = pd.read_csv('tabela.csv')
print(read.to_string(index = False))
