a = float(input("First number: "))
b = float(input("Second number: "))
c = float(input("Third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)
