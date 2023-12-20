from LF05.GrundlageSeite11.printnice import print_nice
# Aufgabe 1 a & b
ok = " ist OK"
# input
user_input = input("String: ")
print_nice(user_input, is_input=True)
print_nice("Das wort kleingeschrieben: ")
output_message = user_input.lower()
print_nice(output_message)
print_nice("Anzahl der Zeichen: ")
count_of_letters = len(user_input)
print_nice(str(count_of_letters))
print_nice(user_input + ok)



