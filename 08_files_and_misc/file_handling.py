# Program: File likhna aur parhna
filename = "sample.txt"

with open(filename, "w") as f:
    f.write("Pehli line\n")
    f.write("Doosri line\n")
    f.write("Teesri line\n")

with open(filename, "a") as f:
    f.write("Chauthi line (append)\n")

with open(filename, "r") as f:
    content = f.read()

print("File ka content:")
print(content)
print("Total lines:", len(content.splitlines()))
