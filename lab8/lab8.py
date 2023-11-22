my_dict = dict()
s = input()
my_list = []
my_list = s.split(', ')
for elem in my_list:
    my_dict[elem] = my_dict.get(elem, 0) + 1


list_v = list(my_dict.values())
list_v = sorted(list_v, reverse = True)
k = len(list_v)
if k <= 3:
    for i in range(k):
        for key, value in my_dict.items():
            if value == list_v[i]:
                print('{}: {}'.format(key, value))
else:
    for i in range(3):
        for key, value in my_dict.items():
            if value == list_v[i]:
                print('{}: {}'.format(key,value))

