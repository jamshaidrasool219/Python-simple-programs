# Program: GCD aur LCM
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


a = int(input("Pehla number: "))
b = int(input("Doosra number: "))

g = gcd(a, b)
print("GCD =", g)
print("LCM =", (a * b) // g)
