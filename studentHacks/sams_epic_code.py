import datetime 
while 1:  
  try:
    #checks to see if your input can be coverted to an int
    DOB = int(input('What year where you born in? '))
    break
  except:
    print('invalid input\n')
date = datetime.datetime.today()
print('You are',date.year - DOB,'years old.\n')
