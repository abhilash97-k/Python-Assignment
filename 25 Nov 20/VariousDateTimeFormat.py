from datetime import datetime
print(datetime.now())
import datetime
now = datetime.datetime.now()
tday = datetime.date.today()
print(now.year)
print(now.month)
year, weak, day = tday.isocalendar()
print(str(weak) + " of " + str(year))
print(str(day) + " of " + str(weak))
x = datetime.datetime.now()
print(x.strftime('%j'))
print(x.strftime('%d'))
print(x.strftime('%w'))