string = input()
ministring = input()
array = string.split()
low_str = ministring.lower()
for i in range(len(array)):
    if low_str in array[i].lower():
        print(array[i])
