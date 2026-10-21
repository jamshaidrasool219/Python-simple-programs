# Program: Number ko ulta karna
n = int(input("Number likhein: "))

rev = 0
temp = abs(n)
while temp > 0:
    rev = rev * 10 + temp % 10
    temp //= 10
print("Reverse =", -rev if n < 0 else rev)
