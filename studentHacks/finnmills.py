import datetime

year = int(input('Enter the year you were born... '))
month = int(input('Enter 1-12 for the month you were born... '))
day = int(input('Enter the day of the month you were born... '))

currentyear = datetime.datetime.today().year
currentmonth = datetime.datetime.today().month
currentday = datetime.datetime.today().day

if day >= currentday:
    currentmonth -= 1
    currentday += 30

if month >= currentmonth:
    currentyear -= 1
    currentmonth += 12

print('You are', + currentyear - year, 'years,', + currentmonth - month, 'months and', + currentday - day, 'days.')

if yes = no
  no = yes
  print out my autobiography
  Sign the papera
