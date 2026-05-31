import time
import os

def clean():
    # clean the console
    # for windows and for linux and mac
    os.system("cls" if os.name == "nt" else "clear")
def crear_archivo():
    # check if the file exists, if not create it
    if os.path.exists("tareas.txt"):
        pass
    else:
        with open("tareas.txt", "x"):
            pass
def mostrar_tarea():
    # read the file and print the content
    tareas = open("tareas.txt","r")
    contenido = tareas.read()
    tareas.close()
    while True:
        clean()
        print(contenido)
        salir_mostrar_tarea = input("INTRODUCE 1 PARA SALIR\n")
        if salir_mostrar_tarea == "1":
            break
        else:
            continue
def agregar_tarea():
    # ask the user to input a task and add it to the file, if the user inputs "salir" exit the function
    while True:
        clean()
        print("ESTO SOLO AGREGA AL ARCHIVO\n")
        print("pon salir, para regresar al inicio \n")
        ingresar_tarea = input("Ingresa tus tareas pendientes\n").lower()
        if ingresar_tarea == "salir":
            break
        else:
            tareas = open("tareas.txt","a")
            tareas.write(ingresar_tarea + "\n")
            tareas.close()
            clean()

            print("tarea recibida")
            time.sleep(2)
            
def vaciar_tarea():
    # Secundary menu to delete all tasks, if the user inputs "1" delete all tasks, if the user inputs "2" exit the function
    while True:
        clean()
        borrar = input(" 1.-Vaciar tareas\n  2.-Salir\n")

        if borrar == "1":
            with open("tareas.txt", "w") as tareas:
                tareas.write("")
            print("TODAS LAS TAREAS ELIMINADAS")
            time.sleep(1)
        elif borrar == "2":
            break
        else:
            print("opcion invalida")
            time.sleep(1)

def deseo_use(deseo):
    # use the input to call the function that the user wants to use
    if deseo == "1":
        agregar_tarea()
    elif deseo == "2":
        vaciar_tarea()
    elif deseo == "3":
        mostrar_tarea()
    elif deseo == "4":
        pass
    else:
        print("opcion invalida")
        time.sleep(1)
def main():
    # main function to call the other functions    
    crear_archivo()
    while True: 
        # principal menu, if the user inputs 
        # "1" call the function to add tasks, if the user inputs 
        # "2" call the function to delete all tasks, if the user inputs 
        # "3" call the function to show tasks, if the user inputs 
        # "4" exit the program
        clean()
        deseo = input("¿Que deseas hacer?\n 1.-Agregar tareas\n 2.-Vaciar tareas\n 3.-Mostrar tareas\n 4.-Salir\n")
        deseo_use(deseo)
        if deseo == "4":
            break

    
if __name__ == "__main__":
    main()