def GetData(filename):
    with open(filename) as f:
        size = int(f.readline().split()[0])
        xs, ys = [[] for i in range(size)], [[] for j in range(size)]
        for i in range(size):
            line = [float(value) for value in f.readline().split()]
            xs[i], ys[i] = line[0], line[1]
        zs = []
        for i in range(size):
            zs.append([float(value) for value in f.readline().split()])
    return xs, ys, zs

def EditData(data, power, givenX):
    from math import fabs
    difs = [fabs(givenX - tableX) for tableX in data[0]]
    result = [[], []]
    for i in range(power + 1):
        ind = difs.index(min(difs))
        difs.pop(ind)
        for i in range(len(data)):
            result[i].append(data[i].pop(ind))
    return result

def SortByX(data):
    for i in range(len(data[0]) - 1):
        for j in range(i + 1, len(data[0])):
            if data[0][i] > data[0][j]:
                for k in range(len(data)):
                    tmp = data[k][i]
                    data[k][i] = data[k][j]
                    data[k][j] = tmp

def CountDivDiff(data):
    #print(data)
    step = 1
    while len(data[-1]) != 1:
        data.append([])
        for i in range(len(data[-2]) - 1):
            data[-1].append((data[-2][i + 1] - data[-2][i]) / (data[0][i + step] - data[0][i]))
        step += 1

def Solve(koefs, tableX, givenX):
    result = 0
    multiple = 1
    for ind, koef in enumerate(koefs):
        result += koef * multiple
        multiple *= (givenX - tableX[ind])
    return result

def Approximate(alldata, n, X):
    from copy import deepcopy as dc
    data = EditData(dc(alldata), n, X)
    SortByX(data)
    CountDivDiff(data)
    koefs = [data[i][0] for i in range(1, len(data))]
    result = Solve(koefs, data[0], X)
    return result
