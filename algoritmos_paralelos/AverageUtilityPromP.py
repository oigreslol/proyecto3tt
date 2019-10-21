#!/usr/bin/python

import csv
import njit

@njit(parallel=True, fastmath=True)
def archivo():
    with open('../data/Data2017EmpresaV2.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        openSum = 0
        closeSum = 0
        dates = []
        opens = []
        high = []
        low = []
        close = []
        volume = []
        for row in readCSV:
            date = row[0]
            op = row[1]
            hig = row[2]
            lo = row[3]
            clos = row[4]
            volum = row[5]

            dates.append(date)
            opens.append(op)
            high.append(hig)
            low.append(lo)
            close.append(clos)
            volume.append(volum)        

        for x in range(len(opens)-1):
            temp = float(opens[x+1])
            openSum = openSum + temp
            openSum = openSum / len(opens)

        for y in range(len(close)-1):
            temp1 = float(close[y+1])
            closeSum = closeSum + temp1
            closeSum = closeSum / len(close)

        print(float(closeSum - openSum))

archivo()
