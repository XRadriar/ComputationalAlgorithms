def GetData(filename):
    with open(filename) as f:
        size = int(f.readline().split()[0])
        data = [[0] * size for i in range(3)]
        for i in range(size):
            data[0][i], data[1][i], data[2][i] = [float(el) for el in f.readline().split()]
    return data

def CountDivDiff(data):
    step = 1
    while len(data[-1]) != 1:
        data.append([])
        for i in range(len(data[-2]) - 1):
            if data[0][i + step] == data[0][i]: data[-1].append(data[1][i])
            else: data[-1].append((data[-2][i + 1] - data[-2][i]) / (data[0][i + step] - data[0][i]))
        step += 1

def Solve(koefs, tableArgs, givenArg):
    result = 0
    multiple = 1
    for ind, koef in enumerate(koefs):
        result += koef * multiple
        multiple *= (givenArg - tableArgs[ind])
    return result

def Format(data, power, givenArg):
    difs = [fabs(givenArg - tableArg) for tableArg in data[0]]
    inds = []
    for i in range(power + 1):
        inds.append(difs.index(min(difs)))
        difs[inds[-1]] = difs[difs.index(max(difs))] + 1
    return [[data[i][j] for j in inds] for i in range(len(data))]

def NewtonAlgorithm(data, power, givenArg):
    data = Format([data[0], data[1]], power, givenArg)
    CountDivDiff(data)
    koefs = [data[i][0] for i in range(1, len(data))]
    return Solve(koefs, data[0], givenArg)

def HermiteFortmat(data):
    size = len(data[0])
    for i in range(0, size * 2, 2):
        for j in range(len(data)):
            data[j].insert(i, data[j][i])

def HermiteAlgorithm(data, power, givenArg):
    data = Format([data[0], data[2], data[1]], power, givenArg)
    HermiteFortmat(data)
    CountDivDiff(data)
    koefs = [data[i][0] for i in range(2, len(data))]
    return Solve(koefs, data[0], givenArg)

def ReverseAlgorithm(data, power):
    data = Format([data[1], data[0]], power, 0)
    CountDivDiff(data)
    koefs = [data[i][0] for i in range(1, len(data))]
    return Solve(koefs, data[0], 0)
