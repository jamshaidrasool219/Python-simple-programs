# Program: Simple Calculator
a = float(input("Pehla number: "))
op = input("Operator (+, -, *, /): ")
b = float(input("Doosra number: "))

if op == "+":
    print("Result =", a + b)
elif op == "-":
    print("Result =", a - b)
elif op == "*":
    print("Result =", a * b)
elif op == "/":
    if b == 0:
        print("Zero se divide nahi kar sakte!")
    else:
        print("Result =", a / b)
else:
    print("Ghalat operator!")
