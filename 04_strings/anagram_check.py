# Program: Do words anagram hain ya nahi
a = input("Pehla word: ").replace(" ", "").lower()
b = input("Doosra word: ").replace(" ", "").lower()

if sorted(a) == sorted(b):
    print("Yeh anagram hain")
else:
    print("Yeh anagram nahi hain")
