import pandas as pd

datafile = pd.read_csv('../../../data/Data2017Empresa.csv', sep=';', index_col='Date', parse_dates=['Date'])

openavrg =  datafile["Open"].mean()
closeavrg = datafile["Close"].mean()

avrgStockValue = closeavrg - openavrg

print(datafile)
print(openavrg)
print(closeavrg)
print(avrgStockValue)
