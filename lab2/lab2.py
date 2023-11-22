sum = 0
a = 0
while a != "":
    if int(a) % 2 == 0:
        sum += int(a)
    a = input()
print(sum)
