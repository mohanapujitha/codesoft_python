todo_list = []

# Function to display the current tasks in the list
def display_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")

# Function to add a task to the list
def add_task(task):
    todo_list.append(task)
    print(f"Task '{task}' added to your to-do list.")

# Function to remove a task from the list by its index
def remove_task(index):
    if index >= 1 and index <= len(todo_list):
        removed_task = todo_list.pop(index - 1)
        print(f"Task '{removed_task}' removed from your to-do list.")
    else:
        print("Invalid index. Please enter a valid index.")

# Main program loop
while True:
    print("\nChoose an option:")
    print("1. Display to-do list")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        display_tasks()
    elif choice == '2':
        task = input("Enter task to add: ")
        add_task(task)
    elif choice == '3':
        index = int(input("Enter index of task to remove: "))
        remove_task(index)
    elif choice == '4':
      print("Exiting program. Goodbye!")
    break
else:
        print("Invalid choice. Please enter a valid option (1-4).")