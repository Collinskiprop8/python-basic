value1=int(input("Please enter the  the first value:"))
value2=int(input("Please enter the second value:"))
operator=input("Please enter your operator:")

if operator =='+':
  print(value1+value2)
elif operator =='-':
  print(value1-value2)
elif operator =='*':
  print(value1*value2)
elif operator =='/':
  print(value1/value2)
else:
  print("Syntax error")
