# #    #-5   -4  -3 -2  -1
# Lista=[10, 6, 40, 32, 90]
# #    # 0   1  2   3   4
# print(Lista)
# print(Lista[2])
# print("-"*30)



# for i in Lista:
#     print(i*2)

# Lista.append(6)
# print("-"*30)


# for i in Lista:
#     print(i*2)


# .insert=insetar elemento
# .remove = borrar un elemento 

#Cree una lista de 4 frutas y muetrelas cada una.

# Lista_frutas=[" manzanas", " limones", " peras", " cocos"]

# print(Lista_frutas)
# print(Lista_frutas[0])
# print("-"*30)

# for i in Lista_frutas:
#     print(i*2)
# Lista_frutas.remove("limones")







pokemons=["ekans", "Gastly"]
def mostrar():
    c=1
for p in pokemons:
    print(c,".-", p)
    c+=1
    
def eliminar():
    mostrar()
borrar_pokemon=input("Ingrese el pokemon a borrar: ")
pokemons.remove(borrar_pokemon)

def actualizar():
    mostrar()
actualizar_pokemon=int(input("Ingrese el pakomen a actualizar: "))
pokemons[actualizar_pokemon-1]=input("Que pokemon va a agregar?: ")
print("Actualizaste el pokemon con exito")

def agregar():
    pokemon_nuevo=input("Ingrese un pokemon: ")
    pokemons.append(pokemon_nuevo)

def menu_pokemon():
    while True:
        try:
            print(".- Agregar Pokemon")
            print(".- Eliminar Pokemon")
            print(".- Actualizar Pokemon")
            print(".- Mostar Pokemon")
            print(".- salir")
            op=int(input("Seleccione una opción: "))
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
                    print("Salir de programa")
                    break

        except ValueError as e:
            print("Solo números enteros")

print(menu_pokemon)

