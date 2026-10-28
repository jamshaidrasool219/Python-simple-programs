# Program: Simple To-Do List
tasks = []

while True:
    print("\n1. Task add karein")
    print("2. Tasks dekhein")
    print("3. Task delete karein")
    print("4. Exit")
    choice = input("Option chunein: ")

    if choice == "1":
        tasks.append(input("Task likhein: "))
        print("Task add ho gaya")
    elif choice == "2":
        if not tasks:
            print("Koi task nahi hai")
        for i, t in enumerate(tasks, 1):
            print(f"{i}. {t}")
    elif choice == "3":
        num = int(input("Kaun sa number delete karna hai? "))
        if 1 <= num <= len(tasks):
            print("Delete hua:", tasks.pop(num - 1))
        else:
            print("Ghalat number")
    elif choice == "4":
        print("Khuda hafiz!")
        break
    else:
        print("Ghalat option")
