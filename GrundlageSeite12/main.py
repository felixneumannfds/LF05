import re

user_password = input("insert pw: ")

with open("userpassword.txt", "w") as f:
    f.write(user_password)

def check_string(s):
    # definiert die passwortvorgaben
    alle_zeichen = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

    # überprüfung der gegebenen Zeichen
    if re.match(alle_zeichen, s):
        return "Dein Password ist stark."
    else:
        return "Dein Passwort ist schwach, es enthälte keine Groß- & kleinbuchstaben, Sonderzeichen und Nummern."



s = user_password + check_string(user_password)
print(check_string(s))