s = input()
array = s.split()
string = ''
for i in range(len(array)):
    if i == len(array) - 1:
        string = string + array[i]
    else:
        string = string + array[i] + '*'
print(string)
