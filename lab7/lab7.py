s = input().lower()
my_list = []
my_list = s.split(',')
my_set = list(set(my_list))
for i in range(len(my_set)):
    if ' ' in my_set[i]:
        my_set[i] = my_set[i][1:]
my_set2 = list(set(my_set))
d = sorted(my_set2)
my_string = ', '.join(d)
print(my_string)
