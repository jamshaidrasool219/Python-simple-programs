# Program: Armstrong number check (jaise 153 = 1^3 + 5^3 + 3^3)
n = int(input("Number likhein: "))

digits = str(n)
power = len(digits)
total = sum(int(d) ** power for d in digits)

if total == n:
    print(n, "Armstrong number hai")
else:
    print(n, "Armstrong number nahi hai")
