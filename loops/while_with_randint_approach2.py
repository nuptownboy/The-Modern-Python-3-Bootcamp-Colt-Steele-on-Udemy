# Steele's Module Between 91 and 92

from random import randint

numbers_list = []

for j in range(10):
    numbers_list.append(randint(1, 10))

for i in numbers_list:
    if i != 5:
        print(i)
        continue
    elif i == 5:
        print(f"You made it! See? {i}")
        break
