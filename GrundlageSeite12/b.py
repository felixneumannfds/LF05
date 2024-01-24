import re

def passwort_pruefen(passwort, min_laenge=8, max_laenge=16, braucht_gross=True, braucht_klein=True, braucht_ziffer=True, braucht_sonder=True):
    if not min_laenge <= len(passwort) <= max_laenge:
        return False

    if braucht_gross and not re.search(r'[A-Z]', passwort):
        return False

    if braucht_klein and not re.search(r'[a-z]', passwort):
        return False

    if braucht_ziffer and not re.search(r'\d', passwort):
        return False

    if braucht_sonder and not re.search(r'[@$!%*?&]', passwort):
        return False

    return True

def hauptprogramm():
    min_laenge = int(input("Bitte geben Sie die minimale Länge ein: "))
    max_laenge = int(input("Bitte geben Sie die maximale Länge ein: "))
    braucht_gross = input("Soll das Passwort einen Großbuchstaben enthalten? (j/n) ") == 'j'
    braucht_klein = input("Soll das Passwort einen Kleinbuchstaben enthalten? (j/n) ") == 'j'
    braucht_ziffer = input("Soll das Passwort eine Ziffer enthalten? (j/n) ") == 'j'
    braucht_sonder = input("Soll das Passwort ein Sonderzeichen enthalten? (j/n) ") == 'j'

    passwort = input("Bitte geben Sie das Passwort ein: ")

    if passwort_pruefen(passwort, min_laenge, max_laenge, braucht_gross, braucht_klein, braucht_ziffer, braucht_sonder):
        print("Das Passwort erfüllt alle Kriterien.")
    else:
        print("Das Passwort erfüllt nicht alle Kriterien.")

if __name__ == "__main__":
    hauptprogramm()
