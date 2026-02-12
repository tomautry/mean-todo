tasks = []
while True:
    print("\nTo-Do List Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Remove a task")
    print("4. Quit")
    choice = input("Enter your choice (1-4): ")
    if choice == "1":
        new_task = input("What task do you want to add, pussy?")
        tasks.append(new_task)
        print("Task added mf")
    elif choice == "2":
        if not tasks:
            print("No tasks yet, dumbass")
        else:
            print("Bro get this shit done please: ")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
    elif choice == "3":
        if not tasks:
            print("No tasks to remove dummy")
        else:
            print("Your tasks:")
            for i, task in enumerate(tasks):
                print(f"{i+1}. {task}")
            remove_num = int(input("Enter the number you want to remove: "))
            if 1 <= remove_num <= len(tasks):
                removed = tasks.pop(remove_num - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid number shit for brains")
    elif choice == "4":
        print("Goodbye bitch boy")
        break
    else:
        print("Choose 1-4 only before I up pole on ur bitchass")
