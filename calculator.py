# creation of calculator.py

# selecting 2 numbers

num1 = int(input("Enter 1st number: "))
num2 = int(input("enter 2nd number: "))

# Asking user what functions do you want to execute

print("what function do you want to use?")

print("for addition enter +"
      "\n for subtraction enter - "
      "\n for multiplication enter *"
      "\n for division enter /"
      "\n find a remainder enter %"
      "\n find quotient enter //"
      "\n find square root of a number enter **")
ch = input("Enter any of these char for specific operation +,-,*,/,%,//,**")

result = 0

# selecting the option that the user wants to perform

if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
elif ch == '%':
    result = num1 % num2
elif ch == '//':
    result = num1 // num2
elif ch == '**':
    result = num1 ** num2
else:
    exit