from time import time

#from mpi4py import MPI
import numpy as np
import pandas as pd

tiempo_inicial = time()

csv_reader = pd.read_csv('../data/Data2017Empresa.csv', delimiter=';').drop(['Date','Open','Low','Close'],axis=1)
data = csv_reader['High']*csv_reader['Volume']
prom = np.mean(data)
print(prom)

tiempo_final = time()

tiempo_ejecucion = tiempo_final - tiempo_inicial

print(tiempo_ejecucion)
