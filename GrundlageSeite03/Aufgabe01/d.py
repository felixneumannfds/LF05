jahr = int(input("Jahreszahl: "))

if jahr % 4 == 0 and jahr % 100 != 0:
    print(jahr, "teilbar durch 4 aber nicht durch 100 SCHALTJAHR ALEEEERT")

elif jahr % 400 == 0:
    print(jahr, "teilbar durch 400  SCHALTJAHR ALEEEERT")

else:
    print("Wiu Wiu Wiu WIU WIU WIU", jahr, "KEIN SCHALTJAHR")




