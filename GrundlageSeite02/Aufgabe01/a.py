import math
TryToSqrt = float(input("num: "))

if TryToSqrt > 0:
    newNum = math.sqrt(TryToSqrt)
    print(newNum)
else:
    print(TryToSqrt, "Nicht lösbar")

