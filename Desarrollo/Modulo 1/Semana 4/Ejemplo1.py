tasks={"tienda":["ir a la tienda", "alta"]}
def error(type):
    if type==1: print("Ingrese un valor valido.")
    elif type==2: print("La tarea ya existe.")
    elif type==3: print("La tarea no existe.")
    elif type==4: print("La lista de tareas está vacia.")
    elif type==5: print("El campo no puede estar vacio.")
def menu(): print("========================"), print("1. Añadir tarea."), print("2. Consultar tarea."), print("3. Actualizar prioridad."), print("4. Eliminar tarea."), print("5. Total de tareas."), print("6. Salir."), print("========================")
def addTask():
    while True:
        title=input("Ingrese un titulo para la tarea: ").lower().strip()
        if title in tasks: error(2)
        elif title=="": error(5)
        else: break
    while True:
        description=input("Escriba una descripcion para la tarea: ").lower().strip()
        if description=="": error(5)
        else: break
    while True:
        priority=input("Escriba la prioridad de la tarea (alta, media o baja): ").lower().strip()
        if priority=="alta" or priority=="media" or priority=="baja": 
            tasks[title]=[description, priority]
            print("Se añadío la tarea correctamente.")
            break
        else: error(1)
def consultTask():
    if tasks.__len__()==0: return error(4)
    while True:
        print("Tareas pendientes:")
        for i in tasks.keys():
            print(i)
        title=input("Ingrese titulo a consultar: ").lower().strip()
        if title=="": error(5)
        elif title not in tasks: error(3)
        else: break
    for i in tasks.keys():
        if title==i: print(f"Descripcion: {tasks[i][0]}"), print(f"Prioridad: {tasks[i][1]}")
def updateTask():
    if tasks.__len__()==0: return error(4)
    while True:
        print("Tareas pendientes:")
        for i in tasks.keys():
            print(i)
        title=input("Ingrese titulo de la tarea a actualizar: ").lower().strip()
        if title=="": error(5)
        elif title not in tasks: error(3)
        else: break
    while True:
        priority=input("Ingrese nueva prioridad para la tarea (alta, media o baja): ").lower().strip()
        if priority=="alta" or priority=="media" or priority=="baja":
            tasks[title][1]=priority
            print("La tarea se actualizó con exito.")
            break
        else: error(1)
def deleteTask():
    if tasks.__len__()==0: return error(4)
    while True:
        print("Tareas pendientes:")
        for i in tasks.keys():
            print(i)
        title=input("Titulo de la tarea a eliminar: ").lower().strip()
        if title=="": error(5)
        elif title not in tasks: error(3)
        else: break
    tasks.pop(title)
    print("La tarea se eliminó con exito.")
def totalTasks():
    if tasks.__len__()==0: return error(4)
    for i in tasks.keys():
        print(i)
    print(f"En total son: {tasks.__len__()}")
    while True:
        priority=input("Ingrese la prioridad a filtrar (alta, media o baja): ").lower().strip()
        if priority=="alta" or priority=="media" or priority=="baja":
            counter=0
            for i in tasks:
                if tasks[i][1]==priority:
                    print(i)
                    counter=+1
            if counter==0: print("No hay tareas con esa prioridad.")
            break
        else: error(1)
while True:
    menu()
    try: 
        decision=int(input("Ingrese la opcion que desea: "))
        if decision==1: addTask()
        elif decision==2: consultTask()
        elif decision==3: updateTask()
        elif decision==4: deleteTask()
        elif decision==5: totalTasks()
        elif decision==6:
            print("Saliendo.")
            break
        else: error(1)
    except ValueError: error(1)