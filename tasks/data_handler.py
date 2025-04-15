import pickle
import os

class DataHandler:
    DATA_FILE = 'tasks.pkl'

    def save_tasks(self, tasks):
        with open(self.DATA_FILE, 'wb') as f:
            pickle.dump(tasks, f)

    def load_tasks(self):
        if os.path.exists(self.DATA_FILE):
            with open(self.DATA_FILE, 'rb') as f:
                return pickle.load(f)
        return []
