import datetime
 
mytime = datetime.time(12, 45, 21)
print(str(mytime.hour) + ":" + str(mytime.minute), "p.m. and", mytime.second, "seconds")
 
thisday = datetime.datetime(2025, 2, 20)
age = thisday.year - 2007
print(age)