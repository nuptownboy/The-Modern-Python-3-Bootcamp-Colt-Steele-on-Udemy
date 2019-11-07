# extracurricular (external) exercise found on the web

for num in range(1, 31):
    if (num % 3 == 0) and (num % 5 == 0):
        print(f"{num} FIZZBUZZ")
    elif num % 3 == 0:
        print(f"{num} Fizz")
    elif num % 5 == 0:
        print(f"{num} Buzz")
