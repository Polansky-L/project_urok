import datetime
HB = input ("dd/mm/yy")
lst = HB.split("/")
print(lst)

mon = datetime.date.today().month
delta_mon = (int(lst[1])-mon)
if delta_mon <0:
    delta_mon+=12