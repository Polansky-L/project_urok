import datetime
HB = input ("dd/mm/yy")
lst = HB.split("/")
print(lst)

mon = datetime.date.today().month
delta_mon = (int(lst[1])-mon)
if delta_mon <0:
    delta_mon+=12

day = datetime.date.today().day
delta_day = (int(lst[0])-day)
if delta_day <0:
    delta_day+=31

print (delta_mon, delta_day)