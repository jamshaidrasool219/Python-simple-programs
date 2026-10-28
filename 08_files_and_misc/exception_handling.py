# Program: Exception handling
try:
    a = int(input("Pehla number: "))
    b = int(input("Doosra number: "))
    print("Result =", a / b)
except ValueError:
    print("Sirf number likhein!")
except ZeroDivisionError:
    print("Zero se divide nahi ho sakta!")
finally:
    print("Program khatam.")
