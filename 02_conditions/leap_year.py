year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "Its a leap year")
else:
    print(year, "Its not a leap year nahi")
