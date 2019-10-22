from time import time

from mpi4py import MPI
import numpy as np
import pandas as pd

tiempo_inicial = time()

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

if rank == 0:
    csv_reader = pd.read_csv('Data2017Empresa.csv', delimiter=';').drop(['Date', 'Open', 'Low', 'Close'], axis=1)
    tamaño = len(csv_reader)
    particion = int(tamaño / size)

    for i in range(1, size):
        tope = ((i + 1) * particion)+1
        if i == size-1:
            if (((i + 1) * particion)+1) != tamaño:
                tope = tamaño+1
        data = csv_reader.iloc[(i * particion)+1:tope]
        comm.send(data, dest=i)
    data = csv_reader.iloc[(rank * particion):((rank + 1) * particion)+1]
    prom = (data['High'] * data['Volume']).sum()
    for i in range(1, size):
        prom2 = comm.recv(source=i)
        prom += prom2
    print("Promedio " + str(prom/tamaño) )
    tiempo_final = time()

    tiempo_ejecucion = tiempo_final - tiempo_inicial

    print(tiempo_ejecucion)
else:
    data = comm.recv(source=0)
    prom = (data['High'] * data['Volume']).sum()
    comm.send(prom, dest=0)