prodructos={
    1:{"nombre":"Uva", "precio": 2000 },
    2:{"nombre":"Palta", "precio": 4000 },
    3:{"nombre":"Pera", "precio": 1500 }
} 


'''
            print("1.- Agregar Producto")
            print("2.- Eliminar Producto")
            print("3.- Actualizar Producto")
            print("4.- Mostrar Productos")
            print("5.- Comprar Productos")
            print("6.- Crear Boleta (calcula IVA) y Salir")
            op=int(input("Seleccione una opcion: "))'''

iva=1.19
op=0
carrito=0

print("1.- Agregar producto al carro")
print("2.- Eliminar producto del carro")
print("3.- Actualizar la cantidad del producto")
print("4.- Mostar productos")
print("5.- comprae productos")
print("6.- crear boleta")
print("7.- Salir")
op=int(input("Seleccione una opción: "))
match op:
    case 1:
        Producto_a_agregar=input("Inserte el producto a agregar al carrito: ")
    case 2:
        print
    case 3:
        print
    case 4:
        print
    case 5:
        print
    case 6:
        print





# pokemons=["ekans", "Gastly"]
# def mostrar():
#     c=1
# for p in pokemons:
#     print(c,".-", p)
#     c+=1
    
# def eliminar():
#     mostrar()
# borrar_pokemon=input("Ingrese el pokemon a borrar: ")
# pokemons.remove(borrar_pokemon)

# def actualizar():
#     mostrar()
# actualizar_pokemon=int(input("Ingrese el pakomen a actualizar: "))
# pokemons[actualizar_pokemon-1]=input("Que pokemon va a agregar?: ")
# print("Actualizaste el pokemon con exito")

# def agregar():
#     pokemon_nuevo=input("Ingrese un pokemon: ")
#     pokemons.append(pokemon_nuevo)

# def menu_pokemon():
#     while True:
#         try:
#             print(".- Agregar Pokemon")
#             print(".- Eliminar Pokemon")
#             print(".- Actualizar Pokemon")
#             print(".- Mostar Pokemon")
#             print(".- salir")
#             op=int(input("Seleccione una opción: "))
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
#                     print("Salir de programa")
#                     break

#         except ValueError as e:
#             print("Solo números enteros")

# print(menu_pokemon)


# pokemons={
# 1:{"nombre":"Ekans", "nivel": 19 },
# 2:{"nombre":"Gastly", "nivel": 18 },
# 2:{"nombre":"Eevee", "nivel": 12 },
# }
# def mostrar():
#     for p, z in pokemons.items:
#         print(f"{p}.- {z}")

# print("-"*30)
# def eliminar():
#     mostrar()
# borrar_pokemon=input("Ingrese el pokemon a borrar: ")
# pokemons.remove(borrar_pokemon)
# del [borrar_pokemon]

# def actualizar():
#     mostrar()
# actualizar_pokemon=int(input("Ingrese el pakomen a actualizar: "))
# pokemons[actualizar_pokemon-1]=input("Que pokemon va a agregar?: ")
# print("Actualizaste el pokemon con exito")

# def agregar():
#     mostrar()
# pokemon_nuevo=input("Ingrese un pokemon: ")
# pokemon_nivel=input("Ingrese el nivel: ")
# pokemons[list(pokemons.keys())[-1]+1]={"nombre": pokemon_nuevo, "nivel": pokemon_nivel}

# def menu_pokemon():
#     while True:
#         try:
#             print("1.- Agregar Pokemon")
#             print("2.- Eliminar Pokemon")
#             print("3.- Actualizar Pokemon")
#             print("4.- Mostar Pokemon")
#             print("5.- salir")
#             op=int(input("Seleccione una opción: "))
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
#                     print("Salir de programa")
#                     break

#         except ValueError as e:
#             print("Solo números enteros")

# print(menu_pokemon)

# https://github.com/diegoroblesrivera/diegoPython/blob/main/002/ejerciciosDiccinarios.py