# Program: Palindrome check
s = input("String likhein: ")
clean = s.replace(" ", "").lower()

if clean == clean[::-1]:
    print("Yeh palindrome hai")
else:
    print("Yeh palindrome nahi hai")
