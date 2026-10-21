# Program: Celsius se Fahrenheit aur Fahrenheit se Celsius
c = float(input("Celsius likhein: "))
print("Fahrenheit =", (c * 9 / 5) + 32)

f = float(input("Fahrenheit likhein: "))
print("Celsius =", round((f - 32) * 5 / 9, 2))
