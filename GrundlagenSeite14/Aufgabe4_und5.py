# Aufgabe 4

def min_zwei_gleich(a, b, c):
    if a == b or a == c or b == c:
        return True
    else:
        return False


print(min_zwei_gleich(1, 2, 3))  # False, keine Zahlen sind gleich
print(min_zwei_gleich(1, 2, 2))  # True, b und c sind gleich
print(min_zwei_gleich(3, 3, 3))  # True, alle Zahlen sind gleich
print(min_zwei_gleich(4, 4, 5))  # True, a und b sind gleich



def gen_zwei_gleich(a, b, c):
    if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        return True
    else:
        return False


print(gen_zwei_gleich(1, 2, 3))  # False, keine Zahlen sind gleich
print(gen_zwei_gleich(1, 2, 2))  # True, gen zwei Zahlen sind gleich
print(gen_zwei_gleich(3, 3, 3))  # False, alle Zahlen sind gleich
print(gen_zwei_gleich(4, 4, 5))  # False, mehr als zwei Zahlen sind gleich