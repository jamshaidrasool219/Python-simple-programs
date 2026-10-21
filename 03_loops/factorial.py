# Program: Factorial nikalna
n = int(input("Number likhein: "))

if n < 0:
    print("Negative number ka factorial nahi hota")
else:
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"{n}! = {fact}")
