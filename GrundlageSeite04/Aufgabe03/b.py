import random

number_to_guess = random.randint (1,50)
game_win = False

while True:
    number_user = int(input('Rate eine Zahl zwischen 1-50: '))

    if number_user == number_to_guess:
        print("Glückwunsch, deine Nummer war richtig")
        break
    else:
        print("Falsch! Aber ich gebe dir einen Tipp:")

        if number_user > number_to_guess:
            print("Deine Zahl ist größer als meine Zufallszahl")
        else:
            print("Deine Zahl ist kleiner als meine Zufallszahl")