import argparse

FILE_NAME = "tasks.txt"

def load_tasks():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for task in tasks:
            file.write(task + "\n")

def list_tasks(tasks):
    if not tasks:
        print("No hay tareas.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks, task):
    tasks.append(task)
    save_tasks(tasks)
    print("Tarea agregada.")

def main():
    parser = argparse.ArgumentParser(
        description="Gestor de tareas en terminal"
    )

    parser.add_argument(
        "--list",
        action="store_true",
        help="Muestra todas las tareas"
    )

    parser.add_argument(
        "--add",
        type=str,
        help="Agrega una nueva tarea"
    )

    args = parser.parse_args()
    tasks = load_tasks()

    if args.list:
        list_tasks(tasks)
    elif args.add:
        add_task(tasks, args.add)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
