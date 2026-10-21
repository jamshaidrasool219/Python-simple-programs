# Program: Marks se grade nikalna
marks = float(input("Marks likhein (0-100): "))

if marks < 0 or marks > 100:
    print("Ghalat marks!")
elif marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: F (Fail)")
