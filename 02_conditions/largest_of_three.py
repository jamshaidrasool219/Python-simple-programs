# Program: Teen numbers mein se sab se bara
a = float(input("Pehla number: "))
b = float(input("Doosra number: "))
c = float(input("Teesra number: "))

if a >= b and a >= c:
    print("Sab se bara:", a)
elif b >= a and b >= c:
    print("Sab se bara:", b)
else:
    print("Sab se bara:", c)
