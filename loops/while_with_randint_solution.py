# Steele's Module Between 91 and 92

# use randint(a, b) to generate a random number between a and b
from random import randint

number = 0  # store random number in here, each time through
i = 0  # i should be incremented by one each iteration

while number != 5:  # keep looping while number is not 5
    i += 1
    # print(i)
    number = randint(1, 10)  # update number to be a new random int from 1-10
    print(number)
