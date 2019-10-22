#!/usr/bin/python

import numpy as np
#from numba import njit
import csv
import time


#@njit(parallel=True, fastmath=True)
def archivo():
    start_time = time.time()
    with open('../data/Data2017Empresa.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        openSum = 0
        closeSum = 0
        opens = []
        close = []
        for row in readCSV:
            op = row[1]
            clos = row[4]
            opens.append(op)
            close.append(clos)
            openP = np.array(opens[1:1566], dtype = float)
            closeP = np.array(close[1:1566], dtype = float)

        for x in range(len(opens)-1):
            temp = float(opens[x+1])
            openSum = openSum + temp
        
        openSum = openSum / len(opens)

        for y in range(len(close)-1):
            temp1 = float(close[y+1])
            closeSum = closeSum + temp1
        
        closeSum = closeSum / len(close)

        avrg = closeSum - openSum
        print("El promedio de crecimiento en una acción es de: ", avrg)
        #print(np.mean(closeP) - np.mean(openP))
        print("El tiempo de ejecucion fue de: %s" % (time.time() - start_time))
        #print(closeP)

archivo()
