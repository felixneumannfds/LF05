noten = []
note = 1


while note != 0:

    note = int(input('Note eingeben, 0 als exit: '))
    if note >= 6 or note <= 1:
        print("Zahlen von 1-6 nur erlaubt")
    if note != 0:
        noten.append(note)
        print('Folgende Noten wurden bisher eingetragen: ', noten)
        print(noten)
    else:
        noten_sum = sum(noten)
        noten_anzahl = len(noten)
        noten_durchschnitt = (noten_sum / noten_anzahl)
        print("Notendurchschnitt: ", noten_durchschnitt)
        break

eins = noten.count(1)
zwei = noten.count(2)
drei = noten.count(3)
vier = noten.count(4)
funf= noten.count(5)
sechs = noten.count(6)

print("Notenspiegel:")
print('Anzahl der Note 1: ', eins)
print('Anzahl der Note 2: ', zwei)
print('Anzahl der Note 3: ', drei)
print('Anzahl der Note 4: ', vier)
print('Anzahl der Note 5: ', funf)
print('Anzahl der Note 6: ', sechs)
