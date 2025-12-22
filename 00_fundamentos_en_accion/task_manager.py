# Lista global donde se almacenarán todas las tareas
# Comienza vacía
tasks = []

# Función que muestra el menú principal en pantalla
def show_menu():
    # Salto de línea para que el menú no se vea pegado a lo anterior
    print("\nGestor de Tareas")

    # Opciones disponibles para el usuario
    print("1. Ver tareas")
    print("2. Agregar tarea")
    print("3. Salir")

# Función que muestra las tareas existentes
def show_tasks():
    # Si la lista tasks está vacía
    # En Python, una lista vacía se evalúa como False
    if not tasks:
        print("No hay tareas aún.")
    else:
        # enumerate recorre la lista y además genera un contador
        # start=1 hace que el conteo empiece en 1 y no en 0
        for i, task in enumerate(tasks, start=1):
            # i  -> número de la tarea
            # task -> texto de la tarea
            print(f"{i}. {task}")

# Función para agregar una nueva tarea
def add_task():
    # input detiene el programa y espera que el usuario escriba algo
    task = input("Escribe la nueva tarea: ")

    # Agrega la tarea escrita a la lista tasks
    tasks.append(task)

    # Confirmación visual para el usuario
    print("Tarea agregada.")

# Bucle infinito
# El programa seguirá corriendo hasta que se use 'break'
while True:
    # Mostrar el menú cada vez que inicia una nueva iteración
    show_menu()

    # Capturar la opción elegida por el usuario
    option = input("Elige una opción: ")

    # Si el usuario elige "1", se muestran las tareas
    if option == "1":
        show_tasks()

    # Si elige "2", se agrega una nueva tarea
    elif option == "2":
        add_task()

    # Si elige "3", se muestra mensaje y se sale del bucle
    elif option == "3":
        print("Hasta luego.")
        break  # rompe el while True y termina el programa

    # Cualquier otro valor no es válido
    else:
        print("Opción inválida.")
