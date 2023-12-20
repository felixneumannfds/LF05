from printnice import print_nice

# Aufgabe 2

password = input("Dein passwort: ")

# length as var
len_password = len(password)

# split variable outputs for length password check
if len_password > 7 and len_password < 17:

    print_nice(f"{password} hat {len_password} zeichen:")
    print_nice("es besteht aus mindestens 8 und maximal 16 Zeichen")

elif len_password < 8:

    print_nice(f"{password} hat {len_password} zeichen:")
    print_nice("es besteht aus weniger als Zeichen")

elif len_password > 16:

    print_nice(f"{password} hat {len_password} zeichen:")
    print_nice("es besteht aus mehr als 16 Zeichen")
