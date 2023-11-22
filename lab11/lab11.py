
def lists_sum(*args, **kwargs):
    sum = 0
    unique = kwargs.get('unique')
    if unique == None:
        unique = False
    if unique == False:
        for elem in args:
            for i in range(len(elem)):
                sum += elem[i]
    else:
        my_list = []
        for elem in args:
            for i in range(len(elem)):
                if elem[i] not in my_list:
                    my_list.append(elem[i])
                    sum += elem[i]
    return sum

lists_sum([1, 2, 1, 2])