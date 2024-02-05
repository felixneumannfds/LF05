# Aufgabe 1
# Definition einer Funktion namens "ausgeben"
# Diese Funktion hat keine Parameter.
def ausgeben():
    print('Vielen Dank für Ihre Teilnahme am Gewinnspiel')
    print('Wir werden Sie bald über die Höhe Ihres Gewinns informieren.')

# Hauptprogramm beginnt hier
# Aufruf der Funktion "ausgeben"
ausgeben()  # Dies ist ein Funktionsaufruf


# Definition einer Funktion namens "ausgeben2"
# Diese Funktion hat die Parameter 'vorname', 'nachname' und 'gewinn'.
def ausgeben2(vorname, nachname, gewinn):
    print('Hallo', vorname, nachname + '!')
    print('Sie haben', gewinn, 'EURO gewonnen!')
    print('Sie und das Finanzamt dürfen sich jetzt freuen!')

# Hauptprogramm beginnt hier
# Aufruf der Funktion "ausgeben2" mit den Parametern 'Claus', 'Thaler', und '4711'
ausgeben2('Claus', 'Thaler', 4711)


# Aufgabe 3
# Definition einer Funktion namens "berechnen_durchschnitt"
# Diese Funktion hat die Parameter 'a' und 'b'.
# Diese Funktion berechnet den Durchschnitt von 'a' und 'b' und gibt ihn zurück.
def berechnen_durchschnitt(a, b):
    schnitt = (a + b) / 2
    return schnitt

# Hauptprogramm beginnt hier
# Aufruf der Funktion "berechnen_durchschnitt" mit den Parametern 3 und 4
# Die Funktion berechnet den Durchschnitt von 3 und 4 und gibt das Ergebnis zurück.
print(berechnen_durchschnitt(3, 4))
