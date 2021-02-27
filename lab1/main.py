#from tabulate import tabulate
from copy import deepcopy as dc
from math import *
from funcs import *
data = GetData("data.txt")
X = 0.525
difs = [fabs(X - x) for x in data[0]]
results = {"Newton": [], "Hermite": [], "Reverse": []}
for i in range(1, 5):
	results["Newton"].append(NewtonAlgorithm(dc(data), i, X))
	results["Hermite"].append(HermiteAlgorithm(dc(data), i, X))
	results["Reverse"].append(ReverseAlgorithm(dc(data), i))
#print(tabulate([results["Newton"], results["Hermite"]]))
#print("Ньютон", results["Newton"])
#print("Эрмит", results["Hermite"])
#print("Обратная интерполяция", results["Reverse"])
