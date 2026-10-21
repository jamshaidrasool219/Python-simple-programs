# Program: Number ke digits ka sum
n = abs(int(input("Number likhein: ")))

total = 0
while n > 0:
    total += n % 10
    n //= 10
print("Digits ka sum =", total)
