import math
from tabulate import tabulate

# Erste Reihe der Tabelle
pq_table = [["h in m", "v in m/s", "v in km/h", "t in s"]]

# Benutzereingabe für maximale Höhe und Schrittweite
max_height = float(input("Geben Sie die maximale Höhe in Metern ein: "))
step = float(input("Geben Sie die Schrittweite für die Höhe ein: "))

# Schleife, um die Tabelle zu füllen
h = 0
while h <= max_height:
    g = 9.81
    v_mps = math.sqrt(2 * 9.8 * h)  # Berechnung für v in m/s
    v_kmph = v_mps * 3.6  # Umrechnung von m/s in km/h
    t = math.sqrt(2 * h / g)
    # Runden auf zwei Dezimalstellen
    h = round(h, 2)
    v_mps = round(v_mps, 2)
    v_kmph = round(v_kmph, 2)
    t = round(t, 2)
    # die ergebnisse der tabelle hinzufügen
    new_data = [h, v_mps, v_kmph, t]
    pq_table.append(new_data)
    h += step
# Die Tabelle drucken
print(tabulate(pq_table, headers='firstrow', tablefmt='fancy_grid'))





