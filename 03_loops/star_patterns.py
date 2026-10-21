# Program: Star patterns
n = int(input("Kitni rows? "))

print("\nRight triangle:")
for i in range(1, n + 1):
    print("*" * i)

print("\nPyramid:")
for i in range(1, n + 1):
    print(" " * (n - i) + "* " * i)

print("\nNumber pattern:")
for i in range(1, n + 1):
    print(" ".join(str(j) for j in range(1, i + 1)))
