array = []
for i in range(5):
    a = int(input())
    array.append(a)
array.sort(reverse = True)
for i in range(5):
    print(array[i])