from time import time

from mpi4py import MPI
import numpy as np
import pandas as pd
from datetime import datetime as dt
tiempo_inicial = time()
fechasIniciales = ['21/07/2010','2/08/2010','1/09/2010','1/10/2010','1/11/2010','1/12/2010','1/12/2010','3/01/2011','1/02/2011','1/03/2011','1/04/2011','2/05/2011','2/06/2011','5/07/2011','2/08/2011','1/09/2011','4/10/2011','1/11/2011','1/12/2011','3/01/2012','1/02/2012','1/03/2012','3/04/2012','2/05/2012','14/06/2012','5/07/2012','1/08/2012','4/09/2012','1/10/2012','1/11/2012','3/12/2012','2/01/2013','1/02/2013','1/03/2013','2/04/2013','2/05/2013','4/06/2013','1/07/2013','1/08/2013','3/09/2013','4/10/2013','1/11/2013','2/12/2013','2/01/2014','3/02/2014','3/03/2014','1/04/2014','1/05/2014','3/06/2014','1/07/2014','1/08/2014','2/09/2014','1/10/2014','5/11/2014','1/12/2014','2/01/2015','2/02/2015','2/03/2015','1/04/2015','1/05/2015','1/06/2015','1/07/2015','3/08/2015','1/09/2015','1/10/2015','2/11/2015','1/12/2015','4/01/2016','1/02/2016','1/03/2016','4/04/2016','2/05/2016','1/06/2016','1/07/2016','3/08/2016','1/09/2016','4/10/2016','1/11/2016','1/12/2016','3/01/2017','1/02/2017','1/03/2017','3/04/2017','1/05/2017','1/06/2017','3/07/2017','1/08/2017','1/09/2017','2/10/2017','1/11/2017',]

tiempo_inicial = time()

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()



facturacion = {}

if rank == 0:
    dataInicial = pd.read_csv('Data2017Empresa.csv', delimiter=';').drop(['Open', 'High', 'Close'], axis=1)
    dataInicial['Date'] = pd.to_datetime(dataInicial['Date'])
    tamaño = len(dataInicial)
    tamañoMeses = len(fechasIniciales)
    particion = int(tamaño / size)
    particionMeses = int(tamañoMeses/size)
    for i in range(1, size):
        tope = ((i + 1) * particion)+1
        mesesIncio = i*particionMeses
        topeMeses = ((i+1)*particionMeses)+1
        if i == size-1:
            if (((i + 1) * particion)+1) != tamaño:
                tope = tamaño+1
            if (((i+1) * particionMeses) + 1) != tamañoMeses:
                topeMeses = tamañoMeses
        data = dataInicial.iloc[(i * particion)+1:tope]
        comm.send(mesesIncio,dest=i,tag = 1)
        comm.send(topeMeses, dest=i, tag=2)
        comm.send(data, dest=i,tag = 3)
    data = dataInicial.iloc[(rank * particion):((rank + 1) * particion)]
    for i in range((rank*particionMeses)+1,((rank+1)*particionMeses)-1):
        mesAnterior = data[(data['Date'] <= dt.strptime(fechasIniciales[i], "%d/%m/%Y")) & (data['Date'] >= dt.strptime(fechasIniciales[i - 1], "%d/%m/%Y"))]['Low'].sum()
        mesActual = data[(data['Date'] <= dt.strptime(fechasIniciales[i + 1], "%d/%m/%Y")) & (data['Date'] >= dt.strptime(fechasIniciales[i], "%d/%m/%Y"))]['Low'].sum()
        if (mesAnterior == 0):
            facturacion[str(dt.strptime(fechasIniciales[i], "%d/%m/%Y").month) + '/' + str(dt.strptime(fechasIniciales[i], "%d/%m/%Y").year)] = round((((mesActual - mesAnterior) / 1) * 100), 2)
        else:
            facturacion[str(dt.strptime(fechasIniciales[i], "%d/%m/%Y").month) + '/' + str(dt.strptime(fechasIniciales[i], "%d/%m/%Y").year)] = round((((mesActual - mesAnterior) / mesAnterior) * 100), 2)
    for i in range(1,size):
        facturacion.update(comm.recv(source=i))
    tiempo_final = time()

    tiempo_ejecucion = tiempo_final - tiempo_inicial

    print(tiempo_ejecucion)
    for x in facturacion:
        print (x, ":", facturacion[x])
else:
    mesesIncio = comm.recv(source= 0 , tag = 1)
    topeMeses = comm.recv(source= 0, tag =2)
    data = comm.recv(source=0, tag=3)
    for i in range(mesesIncio,topeMeses-1):
        mesAnterior = data[(data['Date'] <= dt.strptime(fechasIniciales[i], "%d/%m/%Y")) & (data['Date'] >= dt.strptime(fechasIniciales[i - 1], "%d/%m/%Y"))]['Low'].sum()
        mesActual = data[(data['Date'] <= dt.strptime(fechasIniciales[i + 1], "%d/%m/%Y")) & (data['Date'] >= dt.strptime(fechasIniciales[i], "%d/%m/%Y"))]['Low'].sum()
        if (mesAnterior == 0):
            facturacion[str(dt.strptime(fechasIniciales[i], "%d/%m/%Y").month) + '/' + str(dt.strptime(fechasIniciales[i], "%d/%m/%Y").year)] = round((((mesActual - mesAnterior) / 1) * 100), 2)
        else:
            facturacion[str(dt.strptime(fechasIniciales[i], "%d/%m/%Y").month) + '/' + str(dt.strptime(fechasIniciales[i], "%d/%m/%Y").year)] = round((((mesActual - mesAnterior) / mesAnterior) * 100), 2)
    comm.send(facturacion,dest = 0);