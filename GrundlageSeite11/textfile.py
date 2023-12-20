# 4 b zusatzaufgabe
# function changes every vowel to an 'a'
def only_vowel_a(vowel_changed):
    vowels = "aeiouAEIOU"
    for vowel in vowels:
        vowel_changed = vowel_changed.replace(vowel, 'a')
    return vowel_changed

# file extraction
file_path = 'text.txt'
with open(file_path, 'r') as file:
    # Read the entire contents of the file into a string
    all_vowels = file.read()

# executes the changing function
all_vowels_a = only_vowel_a(all_vowels)  # and puts results to var


# create file & fill it with racism
new_file_path = './created_file.txt'
with open(new_file_path, 'w') as new_file_path:
    new_file_path.write(all_vowels_a)


