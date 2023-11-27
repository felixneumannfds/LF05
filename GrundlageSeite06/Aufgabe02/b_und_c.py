while True:
    number = float(input("Zahl eingeben: "))

    if number > 1:
        print("Sie haben es geschafft...")
        break
    else:
        print("ungültige Zahl")

print(number)


# sinvolle Zahlen als Testeingabe:
# 1, 0, -3, 1.2
# 0 und -3 sind unter der bedingung und provoziert falsche Ausgaben, um zu testen, ob das Programm es registriert und ob
# die Console negative Zahlen mit nem Bindestrich davor erkennt und als negativ wertet. 1 ist die Schwelle, weshalb ich
# gerne die Zahl aus der If - bedingung nochmal teste. 1.2 ist eine richtige Eingabe und überprüft ob dezimale Zahlen
# funktionieren. Damit deckt diese Eingabe auch gleich 2 funktionsweisen des programmes ab
