# Aufgabe 1

# 1.1
temps = []
hour = 0
while hour <= 23:
    print("uhrzeit: ", hour,":00")
    cel = int(input("Temperatur eingeben: "))
    temps.append(cel)
    hour += 1

print(temps)

# 1.2
user_hour = int(input("Stunde eingeben: "))
print("Um", user_hour, ":00 Uhr waren es: ", temps[user_hour], "°C")

# 1.3
average_temp = sum(temps) / len(temps)
print("Durchschnittstemperatur:", average_temp, "°C")
temps.sort(reverse=True)
highest_temp = temps[0]
lowest_temp = temps[23]

print("Höchsttemperatur :", highest_temp, "°C")
print("Tiefstemperatur :", lowest_temp, "°C")

# 1.4
if highest_temp < 0 and lowest_temp < 0:
    print("Eistag")

if lowest_temp < 0 and highest_temp >= 0:
    print("Frosttag")

if lowest_temp >= 0 and highest_temp >= 0:
    print("same shit different day")

