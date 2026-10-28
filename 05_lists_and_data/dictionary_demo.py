# Program: Dictionary ka basic istemal
student = {
    "name": "Ali",
    "age": 20,
    "program": "AI",
}

print("Student:", student)
print("Naam:", student["name"])

student["city"] = "Lahore"
student["age"] = 21

for key, value in student.items():
    print(key, ":", value)
