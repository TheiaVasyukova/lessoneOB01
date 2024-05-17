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

manager = TaskManager()
manager.add_task("Заказать пиццу", "2024-05-17")
manager.add_task("Сходить за кофе с круассаном", "2024-05-17")
manager.add_task("Записаться на маникюр", "2024-05-19")

manager.mark_task_completed("Заказать пиццу")
manager.mark_task_completed("Сходить за кофе с круассаном")

manager.display_tasks()

print("Не выполнено:")
for task in manager.get_pending_tasks():
    print(task.display_info())