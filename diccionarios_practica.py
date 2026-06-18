# Inventario_minecraft={
#     1:{"nombre":"pico de madera", "stacks": 5},
#     2:{"nombre":"piedra", "stacks": 8},
#     3:{"nombre":"madera", "stacks": 2},
#     4:{"nombre":"hierro", "stacks": 3}
# }

# def agregar():
#     print("-"*30)
#     mostrar()
#     print("Agregar recursos")
#     recurso_a_agregar=input("Ingrese un recurso a agregar: ")
#     try:
#         stacks=int(input("Ingrese cuantos stacks agregara: "))
#     except ValueError:
#         print("Cantidad inválida, no puede agregar 0")
#         stacks=0
#     Inventario_minecraft[list(Inventario_minecraft.keys())[-1]+1]={"nombre": recurso_a_agregar, "stacks": stacks }
#     print("-"*30)   

# def eliminar():
#     print("-"*30)
#     mostrar()
#     print("Eliminar recursos")
#     try:
#         borrar_recurso=int(input("Que recurso quiere eliminar ?: "))
#         if borrar_recurso in Inventario_minecraft:
#             del Inventario_minecraft[borrar_recurso]
#         else:
#             print("El recurso no existe")
#     except ValueError:
#         print("Debe ingresar un número valido")


# def actualizar():
#     print("-"*30)
#     mostrar()
#     print("Actualizar recursos")
#     try:
#         recurso_a_actualizar=int(input("Que recurso desea actualizar ?: "))
#         if recurso_a_actualizar in Inventario_minecraft:
#             nombre_recurso=input("Ingrese nombre del recurso: ")
#             stack_actualizar=int(input("ingresa el stack del recurso: "))
#             Inventario_minecraft[recurso_a_actualizar]={"nombre":nombre_recurso, "stack": stack_actualizar }
#             print("Recurso actualizado con exito")
#         else:
#             print("EL recurso no existe")
#     except ValueError:
#         print("Recurso no encontrado")
#     print("-"*30)

# def mostrar():
#     print("-"*30)
#     print("Inventario")
#     for num, stack in Inventario_minecraft.items():
#         print(f"{num}.- {stack["nombre"]} {stack["stacks"]} stacks")

# def Inventario():
#     op=0
#     while True:
#         try:
#             print("-------- Inventario minecraft ---------")
#             print("1.- Agregar recursos ")
#             print("2.- Eliminar recursos")
#             print("3.- Actualizar recursos")
#             print("4.- Mostrar inventario")
#             print("5.- Salir")
#             op=int(input("Elija una opción: "))
#             match op:
#                 case 1:
#                     agregar()

#                 case 2:
#                     eliminar()

#                 case 3:
#                     actualizar()

#                 case 4:
#                     mostrar()

#                 case 5:
#                     print("Saliendo del inventario")
#                     break
#         except ValueError as e:
#             print("Solo números enteros. ERROR", e)


# Inventario()

estuche={
    1:{"nombre":"lapicero", "cantidad": 2},
    2:{"nombre":"goma", "cantidad": 1},
    3:{"nombre":"lapiz mina", "cantidad": 3},
    4:{"nombre":"tijera", "cantidad": 1}
}

print("-------Mostar articulso del estuche-------")
print("1.- agregar articulos")
print("2.- eliminar articulos")
print("3.- actualizar articulos")
print("4.- mostrar articulos")
print("5.- Salir")
op=int(input("Elije una de las opciones: "))
match op:
    case 1:
        print("-"*30)
        print("Agregar ")
        agregar_articulo=input("Ingrese el articulo a agregar:  ")
        try:
            cantidad_de_articulo=int(input("Ingresa la cantidad de articulos: "))
        except ValueError:
            print("ERROR, no puede agregar 0 articulos")
        estuche[list(estuche.keys())[-1]+1]={"nombre":agregar_articulo, "cantidad":cantidad_de_articulo}
    case 2:
        print("-"*30)

        
    case 3:
        print()

    case 4:
        print("Articulos del estuche")
        print("-"*30)
        for num, artic in estuche.items():
            print(f"{num}.- {artic["nombre"]} cantidad: {artic["cantidad"]}")

    case 5:
        print()
