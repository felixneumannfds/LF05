import random
import time
# Materialien für den Baum als Var
empty = " "
star = "*"
bauble_smol = "o"
bauble_big = "O"
trunk = "I"

# list für random pick
tree_mats = [star, bauble_big, star, bauble_smol, star]

# Abfrage Höhe des Baumes
count = int(input("Anzahl der Zeilen eingeben: "))

# vor dem loop noch die höhe speichern um den Stamm am Ende zu platzieren
count_full = count - 1

# Main Loop berechnet leere Stellen anhand der position in Reihe
for x in range(count+1):
    # Abhängig von Reihe
    row = ""
    for i in range(x):
        random_tree_mats = random.choice(tree_mats)
        row += random_tree_mats + " "
    print(count * empty, row)
    count -= 1

# Ausgabe Baumstamm in der Mitte
print(count_full * empty, trunk)
xmas = ("""\
 _   _                          __  __  __  __    _    ____  
| | | | __ _ _ __  _ __  _   _  \ \/ / |  \/  |  / \  / ___| 
| |_| |/ _` | '_ \| '_ \| | | |  \  /  | |\/| | / _ \ \___ \ 
|  _  | (_| | |_) | |_) | |_| |  /  \  | |  | |/ ___ \ ___) |
|_| |_|\__,_| .__/| .__/ \__, | /_/\_\ |_|  |_/_/   \_\____/ 
            |_|   |_|    |___/
""")
print(xmas)
time.sleep(120)