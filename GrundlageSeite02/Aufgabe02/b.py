months = []
for x in range(3):
    turnover = float(input("umsatz: "))
    months.append(turnover)

all = sum(months)

if all > 1000:
    bonus = (2 / 100) * all
else:
    bonus = 0
print("Gesamt: ", all, "€", "Bonus: ", bonus, "€")