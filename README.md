# Smart Todo List with Reminders

**Smart Todo List** is a Python-based task management app with a simple GUI. It lets users create, organize, and manage tasks by category, priority, and deadline. The app also provides smart reminders for tasks due soon, helping you stay on track.

## 🚀 Features
- Add new tasks with:
  - Title
  - Description
  - Category
  - Deadline (YYYY-MM-DD)
  - Priority (1–5)
- View all tasks sorted by priority and deadline
- Mark tasks as completed
- Receive reminders for upcoming tasks
- Save and load tasks from a local file for persistence
- Graphical User Interface (GUI) built with Tkinter

## 📦 Project Structure
```
todoProficiency/
├── gui.py               # GUI interface using Tkinter
├── main.py              # CLI entry point (optional)
├── tasks/
│   ├── task.py
│   ├── task_manager.py
│   ├── data_handler.py
│   ├── reminder.py
│   └── notifier.py
├── requirements.txt     # Required packages (if any)
└── README.md            # Project documentation
```

## 🛠️ Usage
To run the GUI version:
```bash
python gui.py
```

To run the CLI version (if implemented):
```bash
python main.py
```

## 💾 Requirements
- Python 3.7+
- Tkinter (comes pre-installed with standard Python distributions)

Install dependencies (if listed):
```bash
pip install -r requirements.txt
```

## 📌 Future Improvements
- Dark mode support
- Notifications via system tray
- Search/filter functionality
- Deadline countdown timers

---

