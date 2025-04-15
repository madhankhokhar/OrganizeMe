import tkinter as tk
from tkinter import messagebox, ttk
from tasks.task_manager import TaskManager
from tasks.task import Task
import datetime

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Todo List")
        self.manager = TaskManager()

        self.manager.load_tasks()
        self.create_widgets()
        self.refresh_tasks()

    def create_widgets(self):
        # Frame for adding a task
        add_frame = tk.LabelFrame(self.root, text="Add New Task")
        add_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(add_frame, text="Title").grid(row=0, column=0)
        self.title_entry = tk.Entry(add_frame)
        self.title_entry.grid(row=0, column=1)

        tk.Label(add_frame, text="Description").grid(row=1, column=0)
        self.desc_entry = tk.Entry(add_frame)
        self.desc_entry.grid(row=1, column=1)

        tk.Label(add_frame, text="Category").grid(row=2, column=0)
        self.category_entry = tk.Entry(add_frame)
        self.category_entry.grid(row=2, column=1)

        tk.Label(add_frame, text="Deadline (YYYY-MM-DD)").grid(row=3, column=0)
        self.deadline_entry = tk.Entry(add_frame)
        self.deadline_entry.grid(row=3, column=1)

        tk.Label(add_frame, text="Priority (1-5)").grid(row=4, column=0)
        self.priority_entry = tk.Entry(add_frame)
        self.priority_entry.grid(row=4, column=1)

        tk.Button(add_frame, text="Add Task", command=self.add_task).grid(row=5, columnspan=2, pady=5)

        # Treeview for displaying tasks
        self.tree = ttk.Treeview(self.root, columns=("Title", "Description", "Category", "Deadline", "Priority", "Completed"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col)
        self.tree.pack(fill="both", expand=True, padx=10, pady=5)

        # Buttons to manage tasks
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(fill="x", padx=10, pady=5)

        tk.Button(btn_frame, text="Mark as Completed", command=self.complete_task).pack(side="left")
        tk.Button(btn_frame, text="Refresh", command=self.refresh_tasks).pack(side="right")

    def add_task(self):
        try:
            title = self.title_entry.get()
            description = self.desc_entry.get()
            category = self.category_entry.get()
            deadline = datetime.datetime.strptime(self.deadline_entry.get(), "%Y-%m-%d")
            priority = int(self.priority_entry.get())

            new_task = Task(title, description, category, deadline, priority)
            self.manager.add_task(new_task)
            self.manager.save_tasks()
            self.refresh_tasks()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def refresh_tasks(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        self.manager.load_tasks()
        tasks = self.manager.tasks  # Updated here to directly access tasks list
        for task in sorted(tasks, key=lambda t: (t.priority, t.deadline)):
            self.tree.insert("", "end", values=(task.title, task.description, task.category, task.deadline.strftime("%Y-%m-%d"), task.priority, task.completed))

    def complete_task(self):
        selected = self.tree.selection()
        if selected:
            item = self.tree.item(selected[0])
            title = item["values"][0]
            for task in self.manager.tasks:
                if task.title == title:
                    task.completed = True
                    break
            self.manager.save_tasks()
            self.refresh_tasks()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
