birthYear =  int(input('What is your birth year?'))
currentYear = 2019
birthday = (input('true/false, You have had you birthday this year.'))
age = currentYear - birthYear

if birthday == 'true':
  print ('your age is', age)
  
elif birthday == 'false':
  print ('your age is', age -1)

else: 
  print ('please type true or false')

