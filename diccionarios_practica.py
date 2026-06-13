Inventario_minecraft={
    1:{"nombre":"pico de madera", "stacks": 5},
    2:{"nombre":"piedra", "stacks": 8},
    3:{"nombre":"madera", "stacks": 2},
    4:{"nombre":"hierro", "stacks": 3}
}

def agregar():
    print("-"*30)
    mostrar()
    print("Agregar recursos")
    recurso_a_agregar=input("Ingrese un recurso a agregar: ")
    try:
        stacks=int(input("Ingrese cuantos stacks agregara: "))
    except ValueError:
        print("Cantidad inválida, al usar 0")
        stacks=0
    Inventario_minecraft[list(Inventario_minecraft.keys())[-1]+1]={"nombre": recurso_a_agregar, "stacks": stacks }
    print("-"*30)
    

def eliminar():
    print("-"*30)
    mostrar()
    print("Eliminar recursos")
    try:
        borrar_recurso=int(input("Que recurso quiere eliminar ?: "))
        if borrar_recurso in Inventario_minecraft:
            del Inventario_minecraft[borrar_recurso]
        else:
            print("El recurso no existe")
    except ValueError:
        print("Debe ingresar un número valido")
    print("-"*30)


def actualizar():
    print("-"*30)
    mostrar()
    print("Actualizar recursos")
    try:
        recurso_a_actualizar=int(input("Que recurso desea actualizar ?: "))
        if recurso_a_actualizar in Inventario_minecraft:
            nombre_recurso=input("Ingrese nombre del recurso: ")
            stack_actualizar=int(input("ingresa el stack del recurso: "))
            Inventario_minecraft[recurso_a_actualizar]={"nombre":nombre_recurso, "stack": stack_actualizar }
            print("Recurso actualizado con exito")
        else:
            print("EL recurso no existe")
    except ValueError:
        print("Recurso no encontrado")
    print("-"*30)

def mostrar():
    print("-"*30)
    print("Inventario")
    for num, stack in Inventario_minecraft.items():
        print(f"{num}.- {stack["nombre"]} {stack["stacks"]} stacks")

def Inventario():
    op=0
    while True:
        print("-------- Inventario minecraft ---------")
        print("1.- Agregar recursos ")
        print("2.- Eliminar recursos")
        print("3.- Actualizar recursos")
        print("4.- Mostrar inventario")
        print("5.- Salir")
        op=int(input("Elija una opción: "))
        match op:
            case 1:
                agregar()

            case 2:
                eliminar()

            case 3:
                actualizar()

            case 4:
                mostrar()

            case 5:
                print("Saliendo del inventario")
                break


Inventario()

