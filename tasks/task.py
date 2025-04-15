import datetime

class Task:
    def __init__(self, title, description, category, deadline, priority):
        self.title = title
        self.description = description
        self.category = category
        self.deadline = deadline  # datetime object
        self.priority = priority  # Integer (1-5)
        self.completed = False

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title} | Category: {self.category} | Due: {self.deadline.strftime('%Y-%m-%d %H:%M')} | Priority: {self.priority}"
