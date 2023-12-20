from printnice import print_nice

# Aufgabe 3

def mail(user_string):
    return '@' in user_string

def domain(user_string):
    return '.com' in user_string

email = input("Email-Adresse eingebebn: ")

if mail(email) and domain(email):
    print_nice("'@' vorhanden")
    print_nice("'.com' vorhanden")
    print_nice("Diese Adresse scheint legit")

else:
    print_nice("Email-Adresse scheint nicht echt zu sein.")