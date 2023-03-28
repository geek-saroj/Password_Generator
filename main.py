import random
import string

print("welcome to password Generator")


def main():
    length = int(input("Enter the length of password you want: "))
    LowerD = string.ascii_lowercase
    UpperD = string.ascii_uppercase
    DigitD = string.digits
    SymbolD = string.punctuation
    combine = LowerD + UpperD + DigitD + SymbolD
    x = random.sample(combine, length)
    password = "".join(x)
    print(password)
    main()


main()

import itertools
word = "password"
# generate all possible combinations of the word and its variations
combinations = [word, word.upper(), word.lower(), word[::-1]]
for i in range(2, len(word)+1):
    for subset in itertools.combinations(word, i):
        combinations.append("".join(subset))


print(combinations)
