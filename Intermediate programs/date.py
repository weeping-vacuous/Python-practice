import datetime

date= datetime.date(2026,1,2)
today=datetime.date.today()
print(today)

time = datetime.time(12,30,0)
now = datetime.datetime.now()



target_datetime  = datetime.datetime(2030,1,2,12,30,1) 

if target_datetime < now:
    print("The target date has already passed.")
else:
    print("The target date is in the future.")