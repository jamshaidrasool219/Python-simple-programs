# Program: Leap year check
year = int(input("Saal likhein: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "leap year hai")
else:
    print(year, "leap year nahi hai")
