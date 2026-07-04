# Simple To-Do List Application for Beginners
# This program allows users to add, view, mark as complete, and delete tasks

def display_menu():
    """Display the menu options"""
    print("\n=== TO-DO LIST MENU ===")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark task as complete")
    print("4. Delete a task")
    print("5. Quit")
    print("=======================")

def add_task(tasks):
    """Add a new task to the list"""
    task = input("Enter a new task: ").strip()
    if task:
        tasks.append({"task": task, "completed": False})
        print(f"✓ Task '{task}' added!")
    else:
        print("❌ Task cannot be empty!")

def view_tasks(tasks):
    """Display all tasks with their status"""
    if not tasks:
        print("📝 Your to-do list is empty!")
        return

    print("\n📋 YOUR TO-DO LIST:")
    print("-" * 40)
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else " "
        print(f"{i}. [{status}] {task['task']}")
    print("-" * 40)

def mark_complete(tasks):
    """Mark a task as complete"""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            print(f"✓ Task '{tasks[task_num - 1]['task']}' marked as complete!")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")

def delete_task(tasks):
    """Delete a task"""
    view_tasks(tasks)
    if not tasks:
        return

    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"🗑️  Task '{removed_task['task']}' deleted!")
        else:
            print("❌ Invalid task number!")
    except ValueError:
        print("❌ Please enter a valid number!")

def main():
    """Main function to run the to-do list application"""
    tasks = []  # List to store tasks as dictionaries

    print("🎉 Welcome to your To-Do List Application!")

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("👋 Thank you for using the To-Do List Application. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()