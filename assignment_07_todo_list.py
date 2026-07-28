

def display_menu():
    """Prints the main menu options."""
    print("\n============================")
    print("     TO-DO LIST MENU")
    print("============================")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Quit")


def add_task(tasks):
    """
    Prompts user for a task description, adds it to the list,
    and confirms the addition.
    """
    task = input("Enter task: ").strip()
    if task:
        tasks.append(task)
        print(f'Task added: "{task}"')
    else:
        print("Task description cannot be empty.")


def view_tasks(tasks):
    """
    Displays all current tasks numbered from 1.
    If empty, displays a friendly message.
    """
    if not tasks:
        print("Your to-do list is currently empty!")
    else:
        print("\nYour Tasks:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")


def delete_task(tasks):
    """
    Shows current tasks and prompts user for a 1-based index to remove.
    Handles invalid selections gracefully.
    """
    if not tasks:
        print("No tasks available to delete.")
        return

    view_tasks(tasks)
    try:
        task_num = int(input("Enter task number to delete: "))
        # Check if the entered number corresponds to a valid index
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f'Task "{removed_task}" has been removed.')
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Please enter a valid integer task number.")


def main():
    tasks = []

    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4.")



if __name__ == "__main__":
    main()




