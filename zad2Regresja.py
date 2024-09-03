import pandas as pd
import zad2ModulRegresja as reg
import glob
import os.path as osp

for path in glob.glob('./tab_prod_csv/*'):
    bsn = osp.basename(path)
    spltx = osp.splitext(bsn)[0]
    prod = pd.read_csv('./tab_prod_csv/' + spltx + '.csv')
    regr = reg.regresja(prod[['Cena']], prod[['Sprzedaż']])
    print(regr)
