import numpy as np
import pandas as pd

#Zad 1
imiona = pd.ExcelFile('datasets/imiona.xlsx')
df = pd.read_excel(imiona, header=0)
# print(df)

#Zad 2
# print(df[(df.Liczba > 1000)])
# print(df[(df.Imie == 'MATEUSZ')])
# print(df.agg({'Liczba':['sum']}))
# print(df[(df.Rok > 2000) & (df.Rok < 2005)].agg({'Liczba':['sum']}))
# print(df.groupby(['Plec']).agg({'Liczba':['sum']}))
# print(df.groupby(['Rok']))
# print(df.sort_values(by='Liczba'))


#Zad 3
zamowienia = pd.read_csv('datasets/zamowienia.csv', header=0, sep=';', decimal='.')
# print(pd.unique(zamowienia['Sprzedawca']))
# print(zamowienia.groupby(['Sprzedawca']).agg({'idZamowienia':['sum']}))
# print(zamowienia.groupby(['Kraj']).agg({'idZamowienia':['sum']}))
print(zamowienia[('Data Zamowienia' == pd.daterange('2005-01-01', '2005-31-12'))])