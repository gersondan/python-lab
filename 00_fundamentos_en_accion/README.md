Gestor de Tareas en Terminal

Programa en Python que permite:
- Agregar tareas
- Listar tareas
- Interactuar desde la terminal

Objetivo:
Practicar fundamentos de Python creando una herramienta funcional.

Las tareas se guardan automáticamente en un archivo de texto (tasks.txt),
permitiendo que el programa recuerde la información entre ejecuciones.

Persistencia de datos

Uso desde terminal

Listar tareas:
python task_manager.py --list

Agregar tarea:
python task_manager.py --add "Nueva tarea"

Instalación como comando

Dar permisos:
chmod +x tasks

#Mover al PATH:
#mv tasks ~/bin/
Uso:
tasks --list
tasks --add "Nueva tarea"

Eliminar tareas:
tasks --delete 1

La numeración corresponde al orden mostrado con --list
