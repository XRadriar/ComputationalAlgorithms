from prettytable import PrettyTable
from copy import deepcopy as dc
from funcs import *
data = GetData("data.txt")
X = 0.525
results = {"Newton": [], "Hermite": [], "Reverse": []}
for i in range(1, 5):
	results["Newton"].append(round(NewtonAlgorithm(dc(data), i, X), 7))
	results["Hermite"].append(round(HermiteAlgorithm(dc(data), i, X), 7))
	results["Reverse"].append(round(ReverseAlgorithm(dc(data), i), 7))
table = PrettyTable()
table.field_names = ["Степень", "Алгоритм Ньютона", "Алгоритм Эрмита", "Обратная интерполяция"]
table.add_rows([[str(i + 1), results["Newton"][i], results["Hermite"][i], results["Reverse"][i]] for i in range(4)])
print(table)