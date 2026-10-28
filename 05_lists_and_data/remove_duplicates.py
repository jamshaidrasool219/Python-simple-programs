# Program: List se duplicates hatana
items = [1, 2, 2, 3, 4, 4, 5, 1]
print("Original:", items)

unique = []
for i in items:
    if i not in unique:
        unique.append(i)
print("Duplicates ke baghair:", unique)
