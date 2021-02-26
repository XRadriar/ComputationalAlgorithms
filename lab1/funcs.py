def GetData(filename):
    with open(filename) as f:
        size = int(f.readline().split()[0])
        data = [[0] * size for i in range(3)]
        for i in range(size):
            data[0][i], data[2][i], data[1][i] = [float(el) for el in f.readline().split()]
    return data

def EditData(data, power, givenX, hermite=False, reverse=False):
    from math import fabs
    difs = [fabs(givenX - tableX) for tableX in data[0]]
    result = [[], [], []]
    #print("test")
    for i in range(power + 1):
        ind = difs.index(min(difs))
        difs.pop(ind)
        #print(data)
        for i in range(len(data)):
            result[i].append(data[i].pop(ind))
            if hermite:
                result[i].append(result[i][-1])
    if reverse:
        tmp = result[0]
        result[0] = result[2]
        result[2] = tmp
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
    step = 1
    while len(data[-1]) != 1:
        data.append([])
        for i in range(len(data[-2]) - 1):
            if data[0][i + step] == data[0][i]: data[-1].append(data[1][i])
            else: data[-1].append((data[-2][i + 1] - data[-2][i]) / (data[0][i + step] - data[0][i]))
        step += 1

def Solve(koefs, tableX, givenX):
    result = 0
    multiple = 1
    for ind, koef in enumerate(koefs):
        result += koef * multiple
        multiple *= (givenX - tableX[ind])
    return result

def Approximate(alldata, nmin, nmax, X, hermite=False, reverse=False):
    from copy import deepcopy as dc
    result = []
    for n in range(nmin, nmax + 1):
        if hermite: data = EditData(dc(alldata), n, X, hermite=True)
        elif reverse: data = EditData(dc(alldata), n, X, reverse=True)
        else: data = EditData(dc(alldata), n, X)
        #SortByX(data)
        CountDivDiff(data)
        koefs = [data[i][0] for i in range(3, len(data))]
        koefs.insert(0, data[2][0])
        result.append(Solve(koefs, data[0], X))
    return result
