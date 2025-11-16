tasks = []

while True:
    print("\n1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks added yet.")
        else:
            print("Your tasks:")
            for i in range(len(tasks)):
                print(i + 1, tasks[i])

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            print("Your tasks:")
            for i in range(len(tasks)):
                print(i + 1, tasks[i])

            num = int(input("Enter task number to delete: "))
            if num > 0 and num <= len(tasks):
                tasks.pop(num - 1)
                print("Task deleted!")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
