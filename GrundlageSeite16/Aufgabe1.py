def converter(arabic):
    if arabic < 1 or arabic > 7:
        return "Zahl außerhalb des gültigen Bereichs"

    roman = ["I", "II", "III", "IV", "V", "VI", "VII"]
    return roman[arabic - 1]


# Testen der Funktion
for number in range(1, 8):
    print(f"{number} => römisch: {converter(number)}")

