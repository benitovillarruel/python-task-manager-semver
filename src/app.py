tasks = []

def add_task(task):
    tasks.append({
        "name": task,
        "completed": False
    })

def list_tasks():
    if not tasks:
        print("No hay tareas")
        return

    for i, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else "✗"
        print(f"{i}. {task['name']} [{status}]")

add_task("Estudiar Git")
add_task("Practicar SemVer")

list_tasks()