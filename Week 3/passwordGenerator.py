# must be 8 characters
# at least 1 upper case
# at least 1 lower case
# at least 1 number
# at least 1 special character

import random


def passwordGenerator():
    # write code
    lowerchars = ['m', 'e', 'l', 'o']
    upperchars = ['B', 'A', 'L', 'O']

    specialchars = ['%', '@', '!', '#']

    numericchars = ['1', '2', '3', '4']

    password = random.choice(lowerchars) + random.choice(upperchars) + random.choice(specialchars) + random.choice(
        numericchars)

    password = password + password

    return password


print(passwordGenerator())
