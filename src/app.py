tasks = []

def add_task(task):
    if task.strip() == "":
        print("La tarea no puede estar vacía")
        return

    tasks.append({
        "name": task,
        "completed": False
    })

def list_tasks(filter_completed=None):
    if not tasks:
        print("No hay tareas")
        return

    for i, task in enumerate(tasks, start=1):

        if filter_completed is not None:
            if task["completed"] != filter_completed:
                continue

        status = "✓" if task["completed"] else "✗"
        print(f"{i}. {task['name']} [{status}]")

add_task("Practicar ramas")
add_task("")

list_tasks()