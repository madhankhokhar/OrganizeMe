import threading
import datetime
from .notifier import Notifier

class Reminder:
    def __init__(self):
        self.notifier = Notifier()

    def schedule_reminder(self, task):
        now = datetime.datetime.now()
        time_until_deadline = (task.deadline - now).total_seconds()
        reminder_time = time_until_deadline - 3600  # Remind 1 hour before deadline

        if reminder_time > 0:
            timer = threading.Timer(reminder_time, self.send_reminder, [task])
            timer.start()

    def send_reminder(self, task):
        if not task.completed:
            message = f"Reminder: Task '{task.title}' is due at {task.deadline.strftime('%Y-%m-%d %H:%M')}."
            self.notifier.notify(message)
