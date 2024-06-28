def display_menu():
    print("\nSimple To-Do List Application")
    print("1. Add a task")
    print("2. Complete a task")
    print("3. Remove a task")
    print("4. View tasks")
    print("5. Quit")

def add_task(tasks):
    task = input("Enter the task: ")
    tasks.append({'task': task, 'completed': False})
    print(f"Task '{task}' added.")

def complete_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the number of the task to mark as completed: ")) - 1
            if 0 <= task_num < len(tasks):
                tasks[task_num]['completed'] = True
                print(f"Task '{tasks[task_num]['task']}' marked as completed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("Enter the number of the task to remove: ")) - 1
            if 0 <= task_num < len(tasks):
                removed_task = tasks.pop(task_num)
                print(f"Task '{removed_task['task']}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("\nCurrent To-Do List:")
        for i, task in enumerate(tasks):
            status = "Completed" if task['completed'] else "Not completed"
            print(f"{i + 1}. {task['task']} - {status}")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            complete_task(tasks)
        elif choice == '3':
            remove_task(tasks)
        elif choice == '4':
            view_tasks(tasks)
        elif choice == '5':
            print("Quitting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
