import datetime 
while 1:  
  try:
    #checks to see if your input can be coverted to an int
    dob = int(input('What year where you born in? '))
    break
  except:
    print('invalid input\n')
date = datetime.datetime.today()
print('You are',date.year - dob,'years old.\n')
