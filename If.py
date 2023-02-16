# if statement
x=1
marks=49
age=15
grade=39
if(x>0):
  print("The number is positive")
# if... else statement
if(marks>=50):
  print("You have passed the exam")
else:
  print("You have failed your exam")
# if... elif.. else statement
if(grade>=0 and grade<=29):
  print("You failed")
elif grade>=30 and grade<=49:
  print("You have passed")
elif grade>=50 and grade<=79:
  print("You have a credit")
elif grade>=80 and grade<=100:
  print("You have a distiction")
else:
  print("Wrong Grade entered")
# if... elif.. else statement
if(age>=18):
  print("Adult")
elif age<18:
  print("Minor")
else:
  print("None of the above")
# if... elif.. else statement
if(age>=13 and age<=19):
  print("Teenager")
elif age<=12 and age>=0:
  print("Child")
elif age>=19 and age<=28:
  print("Youth")
else:
  print("Adult")
