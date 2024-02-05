# Aufgabe 3
import math


def hypotenuse_berechnen(erste_kathete, zweite_kathete):

    hypotenuse = math.sqrt((erste_kathete * 2) + (zweite_kathete * 2))
    return hypotenuse


print(hypotenuse_berechnen(5, 3))
