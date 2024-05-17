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
