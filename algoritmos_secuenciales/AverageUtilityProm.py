import pandas as pd
import time

start_time = time.time()
datafile = pd.read_csv('../data/Data2017Empresa.csv', sep=';', index_col='Date', parse_dates=['Date'])

openavrg =  datafile["Open"].mean()
closeavrg = datafile["Close"].mean()

avrgStockValue = closeavrg - openavrg

print("El valor promedio de las acciones durante todo el tiempo ha sido de: ", avrgStockValue)
print("--- %s seconds ---" % (time.time() - start_time))
