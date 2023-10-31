# number guesser
import random

number_to_guess = random.randint (1,50)
number_user = int(input('Rate eine Zahl zwischen 1-50: '))

if number_user == number_to_guess:
    print("Glückwunsch, deine Nummer war richtig")
else:
    print("Falsch! Meine Nummer lautete: ", number_to_guess)