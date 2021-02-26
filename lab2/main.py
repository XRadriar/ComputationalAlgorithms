from math import *
from copy import deepcopy as dc
from funcs import *
xs, ys, zs = GetData("data.txt")
#print(zs)
#print(xs, ys)
X = 0.525
N = 3
#difs = [fabs(X - x) for x in data[0]]
for n in range(1, N + 1):
    res = []
    for i in range(len(ys)):
        data = [xs, zs[i]]
        res.append(Approximate(data, n, 1.5))
    data = [ys, res]
    print(Approximate(data, n, 1.5))