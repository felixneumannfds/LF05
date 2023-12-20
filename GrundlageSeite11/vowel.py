# import for better output
from printnice import print_nice

# function changes every vowel to an 'a'
def only_vowel_a(vowel_changed):
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        vowel_changed = vowel_changed.replace(vowel, 'a')
    return vowel_changed


# user input
all_vowels = str(input("Vokale umtauschen auf 'a': "))

# function changes the string
all_vowels_a = only_vowel_a(all_vowels)
# input and changed string output
print_nice(all_vowels)
print_nice(all_vowels_a)
