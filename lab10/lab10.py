import datetime

def gift_count(budget,month,birthdays):
    my_birthdays = dict()
    counter = 0
    podarok = 0
    my_date1 = []
    for elem in birthdays:
        my_date = birthdays.get(elem).strftime('%d.%m.%Y')
        print(my_date)
        if my_date[3:4] == '0':
            my_month = int(my_date[4:5])
        else:
            my_month = int(my_date[3:5])
        if month == my_month:
            counter += 1
            my_birthdays[elem] = my_date
            my_date1.append(my_date)
    if counter == 0:
        print('В этом месяце нет именинников.')
    else:
        podarok = budget // counter
        imeniniki = ', '.join(['{0} ({1})'.format(k,v) for k, v in my_birthdays.items()])

        print(imeniniki)
        print('Именинники в месяце {}: {}. При бюджете {} они получат по {} рублей.'.format(month,imeniniki,budget, podarok))
        print(my_birthdays)
        print(podarok)

birthdays = {"Иванов Иван Иванович": datetime.date(1989, 5, 1), "Петров Петр Петрович": datetime.date(1998, 5, 6)}
gift_count(20007, 5, birthdays)