import datetime
s = input()
date = datetime.datetime.strptime(s, "%d-%m-%Y")
day = date.weekday()
if day == 0:
    print(s)
else:
    date1 = date - datetime.timedelta(days = day)
    day1 = date1.day
    month = date1.month
    year = date1.year
    if month < 10:
        print("{}-0{}-{}".format(day1,month,year))
    else:
        print("{}-{}-{}".format(day1, month, year))

