from tasks.task_manager import TaskManager

def main():
    manager = TaskManager()
    manager.load_tasks()
    manager.start_reminders()

    while True:
        print("\n--- Smart Todo List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == '1':
            manager.add_task()
        elif choice == '2':
            manager.view_tasks()
        elif choice == '3':
            manager.complete_task()
        elif choice == '4':
            manager.save_tasks()
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
