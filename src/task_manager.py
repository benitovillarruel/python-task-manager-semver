class TaskManager:

    def __init__(self):
        self.tasks = []

    def create_task(self, name, status=False):

        if not name.strip():
            raise ValueError("Nombre inválido")

        self.tasks.append({
            "title": name,
            "status": status
        })

    def show_tasks(self):

        if not self.tasks:
            print("Sin tareas")
            return

        for index, task in enumerate(self.tasks, start=1):
            status = "✓" if task["status"] else "✗"
            print(f"{index}. {task['title']} [{status}]")


manager = TaskManager()

manager.create_task("Preparar release 2.0")
manager.show_tasks()