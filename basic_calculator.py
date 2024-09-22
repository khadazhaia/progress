num1 = int(input("enter a number: "))
oper = input("select + , - , * or /: ")
num2 = int(input("enter a number: "))

if oper == "+":
   print(num1 + num2)
elif oper == "-":
   print(num1 - num2)
elif oper == "*":
   print(num1 * num2)
elif oper == "/":
   print(num1 / num2)
else:
   print('Error')
