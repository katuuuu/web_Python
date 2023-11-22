
def get_popular_name_from_file(filename):
    names = dict()
    stroki = []
    with open(filename) as f:
        for line in f:
            stroka = line.split(' ')
            stroki.append(stroka[0])
    for i in range(len(stroki)):
        if stroki[i] not in names:
            names[stroki[i]] = 1
        else:
            names[stroki[i]] = names.get(stroki[i],0) + 1
    mvalue = max(names.values())
    mname = dict()
    for key, value in names.items():
        if value == mvalue:
            mname[key] = value
    return ', '.join(['{0}'.format(k) for k in mname.keys()])