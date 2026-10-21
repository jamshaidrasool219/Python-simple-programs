a = float(input("First number: "))
op = input("Operator (+, -, *, /): ")
b = float(input("Second number: "))

if op == "+":
    print("Result =", a + b)
elif op == "-":
    print("Result =", a - b)
elif op == "*":
    print("Result =", a * b)
elif op == "/":
    if b == 0:
        print("Do not divide it with zero!")
    else:
        print("Result =", a / b)
else:
    print("Wrong operator!")
