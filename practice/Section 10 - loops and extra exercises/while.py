num = 0
while num < 31:
    if (num % 3 == 0) and (num % 5 == 0):
        print(f"{num} FOOBAR")
    elif num % 3 == 0:
        print(f"{num} Foo")
    elif num % 5 == 0:
        print(f"{num} Bar")
    num += 1
print("------------")
