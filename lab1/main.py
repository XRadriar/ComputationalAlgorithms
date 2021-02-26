from math import *
from copy import deepcopy as dc
from funcs import *
data = GetData("data.txt")
X = 0.525
difs = [fabs(X - x) for x in data[0]]
results = {}
results["Newton"] = Approximate(data, 1, 4, X)
results["Hermite"] = Approximate(data, 1, 4, X, hermite=True)
results["Reverse"] = Approximate(data, 1, 7, 0, reverse=True)
print(results["Newton"])
print(results["Hermite"])
print(results["Reverse"])