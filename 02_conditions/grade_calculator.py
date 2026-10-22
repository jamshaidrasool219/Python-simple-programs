marks = float(input("Enter your Marks (0-100): "))

if marks < 0 or marks > 100:
    print("Wrong range of marks!")
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
