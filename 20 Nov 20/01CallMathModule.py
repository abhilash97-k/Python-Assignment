import MathModule

a  = int(input("Enter first number"))
b = int(input("Enter second number"))

print("Please enter a respected operator for mathematical operation +   -   *   /")
ch = input()
if ch == '+':
    print(MathModule.add(a, b))

elif ch == '-':
    print(MathModule.sub(a, b))

elif ch == '*':
    print(MathModule.mul(a, b))

elif ch == '/':
    print(MathModule.div(a, b))

else:
    print("Invalid Operator")