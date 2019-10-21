import csv
from numba import njit

@njit(parallel=True, fastmath=True)
def archivo():
    with open('../data/Data2017EmpresaV2.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
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

archivo()