input_word = str(input())
length_of_word = len(input_word)
letters_read = {}

for letter in input_word:
    if letter in letters_read:
        letters_read[letter] += 1
    else:
        letters_read[letter] = 1

even_letters = 0

for key in letters_read:
    if letters_read[key]%2 == 1:
        even_letters += 1

if even_letters >= 2:
    print('NO')

elif even_letters == 1 and length_of_word%2 == 0:
    print('N0')

elif even_letters == 1 and length_of_word%2 == 1:
    print('YES')

elif even_letters == 0:
    print('YES')