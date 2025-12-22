# Nombre del archivo donde se guardarán las tareas
# Es una constante por convención (mayúsculas)
FILE_NAME = "tasks.txt"


# Función que carga las tareas desde el archivo
def load_tasks():
    try:
        # Abrimos el archivo en modo lectura ("r")
        # encoding="utf-8" permite usar tildes y caracteres especiales
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            
            # file.readlines() devuelve una lista de líneas del archivo
            # Cada línea termina con "\n", por eso usamos strip()
            # strip() elimina espacios y saltos de línea
            return [line.strip() for line in file.readlines()]
    
    # Si el archivo no existe, Python lanza este error
    # En ese caso, devolvemos una lista vacía
    except FileNotFoundError:
        return []


# Función que guarda las tareas en el archivo
def save_tasks(tasks):
    # Abrimos el archivo en modo escritura ("w")
    # Esto sobrescribe el contenido anterior
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        
        # Recorremos cada tarea de la lista
        for task in tasks:
            # Escribimos la tarea en el archivo
            # "\n" crea una nueva línea por cada tarea
            file.write(task + "\n")


# Función que muestra el menú principal
def show_menu():
    print("\nGestor de Tareas")
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Salir")


# Función que muestra las tareas en pantalla
def show_tasks(tasks):
    # Si la lista está vacía
    if not tasks:
        print("No hay tareas aún.")
    else:
        # enumerate recorre la lista y genera un contador
        # start=1 hace que el conteo sea humano (1, 2, 3...)
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")


# Función que agrega una nueva tarea
def add_task(tasks):
    # Pedimos al usuario que escriba la tarea
    task = input("Escribe la nueva tarea: ")
    
    # Agregamos la tarea al final de la lista
    tasks.append(task)
    
    # Guardamos inmediatamente la lista actualizada en el archivo
    save_tasks(tasks)
    
    # Confirmación visual
    print("Tarea agregada y guardada.")


# Cargamos las tareas desde el archivo al iniciar el programa
# Si el archivo no existe, recibimos una lista vacía
tasks = load_tasks()


# Bucle principal del programa
# Se ejecuta indefinidamente hasta que el usuario decida salir
while True:
    show_menu()
    
    # Capturamos la opción elegida por el usuario
    option = input("Elige una opción: ")

    # Opción para ver tareas
    if option == "1":
        show_tasks(tasks)

    # Opción para agregar una nueva tarea
    elif option == "2":
        add_task(tasks)

    # Opción para salir del programa
    elif option == "3":
        print("Hasta luego.")
        break  # Rompe el bucle y termina el programa

    # Cualquier otra entrada no es válida
    else:
        print("Opción inválida.")
