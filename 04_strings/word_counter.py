# Program: Words ginna aur har word kitni baar aaya
text = input("Sentence likhein: ").lower()
words = text.split()

print("Total words:", len(words))

count = {}
for w in words:
    count[w] = count.get(w, 0) + 1

for word, c in count.items():
    print(word, "->", c)
