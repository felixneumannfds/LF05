# speichert eingegebenen Noten
noten = []
# main loop bis 0 eingabe erfolgt
note = 1
while note != 0:
        note = input('Note eingeben: ')
        if note != 0:
            noten.append(note)
            print(input)
            print('Folgende Noten wurden bisher eingetragen: ', noten)
        else:
            print("Eingabe für Noten wurde gestoppt")
            noten.remove('0')
            break



anzahl = len(noten)
sum = sum(noten)

noten_durchschnitt = sum/anzahl
print('Der Notendurchschnitt lautet: ', noten_durchschnitt)

# Notenspiegel

eins= 1
zwei = 2
drei = 3
vier = 4
funf = 5
sechs = 6

notenspiegel = noten.count(eins)
print(notenspiegel)

