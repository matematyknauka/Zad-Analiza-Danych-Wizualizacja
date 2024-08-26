import pandas as pd

df_csv = pd.read_csv('tabela.csv')
print("Statystyki opisowe dla kolumny Cena:\n")

print(f"Średnia: {df_csv['Cena'].mean()}")
print(f"Odchylenie standardowe: {df_csv['Cena'].std()}")
print(f"Moda (ta najmniejsza) {df_csv['Cena'].mode()[0]}")
print(f"Mediana: {df_csv['Cena'].median()}")
print(f"Min: {df_csv['Cena'].min()}")
print(f"Max: {df_csv['Cena'].max()}")
print("\nStatystyki opisowe dla kolumny Zysk:\n")

print(f"Średnia: {df_csv['Zysk'].mean()}")
print(f"Odchylenie standardowe: {df_csv['Zysk'].std()}")
print(f"Moda (ta najmniejsza) {df_csv['Zysk'].mode()[0]}")
print(f"Mediana: {df_csv['Zysk'].median()}")
print(f"Min: {df_csv['Zysk'].min()}")
print(f"Max: {df_csv['Zysk'].max()}")