class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.is_completed = False

    def mark_completed(self):
        self.is_completed = True

    def display_info(self):
        status = "Выполнено" if self.is_completed else "Не выполнено"
        return f"Задача: {self.description}, Срок выполнения: {self.due_date}, Статус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, description, due_date):
        if description not in self.tasks:
            self.tasks[description] = Task(description, due_date)

    def mark_task_completed(self, description):
        if description in self.tasks:
            self.tasks[description].mark_completed()

    def get_pending_tasks(self):
        return [task for task in self.tasks.values() if not task.is_completed]

    def display_tasks(self):
        for task in self.tasks.values():
            print(task.display_info())

