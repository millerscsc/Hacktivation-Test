import datetime, time

year = int(input('What year were you born?'))
month = int(input('What month were you born?'))
day = int(input('What day were you born?'))


print("your age would happen to be")
time.sleep(1)
print(datetime.datetime.today().day - day, "Days old")
time.sleep(1)
print(datetime.datetime.today().month - month, "Months old")
time.sleep(1)
print(datetime.datetime.today().year - year, "Years old")
