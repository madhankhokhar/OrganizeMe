from .task import Task
from .data_handler import DataHandler
from .reminder import Reminder

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.data_handler = DataHandler()
        self.reminder = Reminder()

    def load_tasks(self):
        self.tasks = self.data_handler.load_tasks()

    def save_tasks(self):
        self.data_handler.save_tasks(self.tasks)

    def add_task(self):
        print("\n--- Add New Task ---")
        title = input("Title: ")
        description = input("Description: ")
        category = input("Category: ")
        deadline_str = input("Deadline (YYYY-MM-DD HH:MM): ")
        priority = int(input("Priority (1-5, 1=High): "))

        try:
            deadline = datetime.datetime.strptime(deadline_str, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Invalid date format.")
            return

        task = Task(title, description, category, deadline, priority)
        self.tasks.append(task)
        self.reminder.schedule_reminder(task)
        print("Task added successfully.")

    def view_tasks(self):
        print("\n--- Your Tasks ---")
        if not self.tasks:
            print("No tasks available.")
            return

        sorted_tasks = sorted(
            [t for t in self.tasks if not t.completed],
            key=lambda x: (x.priority, x.deadline)
        )

        for idx, task in enumerate(sorted_tasks, 1):
            print(f"{idx}. {task}")

    def complete_task(self):
        self.view_tasks()
        if not self.tasks:
            return

        try:
            task_num = int(input("\nEnter the task number to complete: "))
            task = [t for t in self.tasks if not t.completed][task_num - 1]
            task.completed = True
            print("Task marked as completed.")
        except (IndexError, ValueError):
            print("Invalid task number.")

    def start_reminders(self):
        for task in self.tasks:
            if not task.completed:
                self.reminder.schedule_reminder(task)
