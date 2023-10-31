import math

# Loop-Stop bei positiver Zahl
ergebnis = False

# Loop für Wiedereingabe, falls Zahl negativ
while ergebnis == False:
    # user zahl request
    zahl = float(input('Deine Zahl: '))
    # fehlermeldung bei negativen Zahlen
    if zahl <= 0:
        print("Zahl darf nicht negativ oder null sein")
    else:
        zahl_neu = math.sqrt(zahl)
        print("Deine Zahl lautete: ", zahl, "Und dessen Quadratwurzel lautet: ", zahl_neu)
        # programm stoppt bei erfolg
        ergebnis = True





