# Materialien für den Baum als Var
empty = " "
star = "*"
trunk = "I"
# Abfrage Höhe des Baumes
count = int(input("Anzahl der Zeilen eingeben: "))
# vor dem loop noch die höhe speichern um den Stamm am Ende zu platzieren
count_full = count - 1

# Main Loop berechnet leere Stellen anhand der position in Reihe
for x in range(count+1):
    print(count * empty, x * star + (x - 1) * star)
    count -= 1
# Ausgabe Baumstamm in der Mitte
print(count_full * empty, trunk)

# kleines Extra im Extra ASCII
xmas = ("""\
 _   _                          __  __  __  __    _    ____  
| | | | __ _ _ __  _ __  _   _  \ \/ / |  \/  |  / \  / ___| 
| |_| |/ _` | '_ \| '_ \| | | |  \  /  | |\/| | / _ \ \___ \ 
|  _  | (_| | |_) | |_) | |_| |  /  \  | |  | |/ ___ \ ___) |
|_| |_|\__,_| .__/| .__/ \__, | /_/\_\ |_|  |_/_/   \_\____/ 
            |_|   |_|    |___/
""")
print(xmas)


