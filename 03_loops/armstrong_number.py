n = int(input("Enter Number: "))

digits = str(n)
power = len(digits)
total = sum(int(d) ** power for d in digits)

if total == n:
    print(n, "Armstrong number hai")
else:
    print(n, "Armstrong number nahi hai")
