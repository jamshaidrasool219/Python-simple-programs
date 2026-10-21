# Program: String ko ulta karna
s = input("String likhein: ")
print("Reverse:", s[::-1])
print("Words ulte:", " ".join(s.split()[::-1]))
