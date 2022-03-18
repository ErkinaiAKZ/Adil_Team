#4
d = input('date(year-month-day h:min): ')
date = {}
date['year'] = d[:4]
date['month'] = d[5:7]
date['day'] = d[8:10]
date['hours'] = d[11:13]
date['minutes'] = d[14:]
print(date)
