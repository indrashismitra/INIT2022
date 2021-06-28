num1 = input("enter the first number")
num2 = input("enter the second number")
sign = input("+, -, / or *")

if sign == "+":
    print(num1 + num2)
elif sign == "-":
    print(int(num1) - int(num2))
elif sign == "/":
    print(int(num1) / int(num2))
elif sign == "*":
    print(num1 * int(num2))
else:
    print("invalid sign")