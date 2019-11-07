# Steele's Module 90

answer = input("How's it going? >> \n")
repeat = answer
while True:
    answer = input(repeat + " >> \n")
    repeat = answer
    if answer.lower() == "stop copying me":
        print("UGH, FINE, YOU WIN!")
        break
    else:
        continue
