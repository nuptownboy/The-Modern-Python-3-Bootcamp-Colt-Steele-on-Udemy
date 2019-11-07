# Steele's Module 89

''' num_list = list(range(11))
print(num_list)
for item in num_list:
    for asterisk in item:
    print('*')'''
num_list = []
x = 1
while x <= 10:
    num_list.append(x)
    # print(num_list)
    print(x*" \U0001f600 ")
    x += 1
