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







         




























# productos={
#     1:{"nombre":"Uva", "precio": 2000 },
#     2:{"nombre":"Palta", "precio": 4000 },
#     3:{"nombre":"Pera", "precio": 1500 }
# }
# carrito=[]
# def mostrar():
#     for num, prod in productos.items():
#         print(f"{num}.- {prod['nombre']}  ${prod['precio']}")
#     print("-"*30)
# def eliminar():
#     mostrar()
#     try:
#         borrar_producto=int(input("Cual es el producto que va a eliminar ?: "))
#         if borrar_producto in productos:
#             del productos[borrar_producto]
#         else:
#             print("Producto no existe")
#     except ValueError:
#         print("Debe ingresar un número válido")
# def actualizar():
#     mostrar()
#     try:
#         key=int(input("que producto desea actualizar: "))
#         if key in productos:
#             nombre=input("Ingrese el nombre del producto: ")
#             precio=int(input("Ingrese el precio del producto: "))
#             productos[key]={"nombre":nombre, "precio": precio }
#             print("actualizado con exito")
#         else:
#             print("Producto no existe")
#     except ValueError:
#         print("ID o precio inválido")
# def agregar():
#     pkm=input("Ingrese el nombre del producto: ")
#     try:
#         nvl=int(input("Ingrese el precio del producto: "))
#     except ValueError:
#         print("Precio inválido, usando 0")
#         nvl=0
#     productos[list(productos.keys())[-1]+1]={"nombre":pkm, "precio": nvl }
# def comprar():
#     while True:
#         mostrar()
#         try:
#             comprar=int(input("Cual producto desea comprar ? ( para salir, ponga 0): "))
#             if comprar==0:
#                 break
#             if comprar in productos:
#                 print(f"Usted ha comprado {productos[comprar]['nombre']} por un valor de {productos[comprar]['precio']}")
#                 carrito.append(productos[comprar])
#             else:
#                 print("Producto no existe")
#         except ValueError:
#             print("Debe ingresar un número válido")
# def boleta():
#     total=0
#     print("-"*30, "0", "-"*30)
#     print("Bienvenido a minimarquet Lost Woods")
#     print("-"*30, "0", "-"*30)
#     for p in carrito:
#         total+=int(p["precio"])
#         print(p["nombre"],"---$", p["precio"])
#     iva=total*0.19
#     print("-"*30, "0", "-"*30)
#     print(f"El total de su compra es {total} y el IVA es {iva}")
#     print(f"El total a pagar es  {total+iva} ")
#     print("Gracias por comprar en minimarquet Lost Woods")
#     print("-"*30, "0", "-"*30)

# def menuProductos():
#     while True:
#         try:
#             print("1.- Agregar Producto")
#             print("2.- Eliminar Producto")
#             print("3.- Actualizar Producto")
#             print("4.- Mostrar Productos")
#             print("5.- Comprar Productos")
#             print("6.- Crear Boleta (calcula IVA) y Salir")
#             op=int(input("Seleccione una opcion: "))
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
#                     comprar()
#                 case 6:
#                     boleta()
#                     break
#                 case _:
#                     print("Opcion Invalida")

#         except ValueError as e:
#             print("Solo numeros enteros. Error",e)


# menuProductos()
