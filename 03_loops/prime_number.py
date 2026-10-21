# Program: Prime number check
n = int(input("Number likhein: "))

if n < 2:
    print(n, "prime nahi hai")
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    print(n, "prime hai" if is_prime else "prime nahi hai")
