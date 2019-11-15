# Steele's Module Between 91 and 92

from random import randint

number = 0
i = 0
for i in randint(1, 10):
    i += 1
    if i == 5:
        print("you reached 3!")
        break
    else:
        continue
