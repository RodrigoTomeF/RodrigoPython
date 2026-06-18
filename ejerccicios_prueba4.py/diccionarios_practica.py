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
#         print("Cantidad inválida, al usar 0")
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
#     print("-"*30)


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
#         print("-------- Inventario minecraft ---------")
#         print("1.- Agregar recursos ")
#         print("2.- Eliminar recursos")
#         print("3.- Actualizar recursos")
#         print("4.- Mostrar inventario")
#         print("5.- Salir")
#         op=int(input("Elija una opción: "))
#         match op:
#             case 1:
#                 agregar()

#             case 2:
#                 eliminar()

#             case 3:
#                 actualizar()

#             case 4:
#                 mostrar()

#             case 5:
#                 print("Saliendo del inventario")
#                 break


# Inventario()








## crear un gestor de estacionamiento
# Un estacionamiento tiene 4 pisos
# y cada piso tiene 10 espacios
#  Preguntar cuando entra un vehiculo, que tipo de vheiculo es
# vehículo ligero 2000
# vehículo mediano 3000
# vehículo pesado 3500
# luego , acomodarlo en algun lugar de algun piso disponible.
# el menu dsebe tener las sigueintes alternativas
# ''' 1.- ingresar vehiculo
# 2.- contar ganancias
# 3.- contar vehiculos'''
# # usa lista o diccionario segun le acomode mas
# parking={
#     1:[2000, 3500, 2000,2000, 3500, 2000,2000, 3500, 2000],
#     2:[], 
#     3:[],
#     4:[]
#}

# estacionamientos={
#             1:[],
#             2:[],
#             3:[],
#             4:[]
# }

# def mostrar():
#     for num, cantidad in estacionamientos.items():
#         print(f"{num} {cantidad}")


# def precios():
#     print("1.- ligero 2000")
#     print("2.- mediano 3000")
#     print("3.- pesado 3500")


# contador_de_vehiculos=0
# ligero=2000
# mediano=3000
# pesado=3500

# contador_de_ganancias=0

# while True:

#     print("-"*30)
#     print("1.- Ingresa vehiculo")
#     print("2.- Contar ganancias")
#     print("3.- Contar vehiculos")
#     print("4.- Salir del gestar de estacionaminto")
#     op=int(input("Elija una de las opciones: "))
#     match op:
#         case 1:
#             print("-"*30)
#             print("Ingresar vehiculo")
#             precios()
#             tipo_de_vehiculo=int(input("Ingrese el tipo de vehiculo: "))

#             numero_de_estacionamiento=int(input("Ingresa piso (1/4)"))
             
#             if tipo_de_vehiculo == 1:
#                 contador_de_vehiculos = contador_de_vehiculos + 1
#                 contador_de_ganancias = contador_de_ganancias + ligero
#                 estacionamientos[numero_de_estacionamiento].append(ligero)
#             elif tipo_de_vehiculo == 2:
#                 contador_de_vehiculos = contador_de_vehiculos + 1
#                 contador_de_ganancias = contador_de_ganancias + mediano
#                 estacionamientos[numero_de_estacionamiento].append(mediano)
#             elif tipo_de_vehiculo == 3:
#                 contador_de_vehiculos = contador_de_vehiculos + 1
#                 contador_de_ganancias = contador_de_ganancias + pesado
#                 estacionamientos[numero_de_estacionamiento].append(pesado)
            
#         case 2:
#             print("-"*30)
#             print("Ganancias")
#             print(f"{sum(list)} son las ganancias por el estacionamiento")
#             for 

#         case 3:
#             print("Cantidad de vehiculos")
#             mostrar()
#             print(f"La cantidad de vehiculos es de {contador_de_vehiculos}")

#         case 4:
#             print("Salir del programa")
#             break


# parking={
#     1:[2000, 3500, 2000,2000, 3500, 2000,2000, 3500, 2000],
#     2:[],
#     3:[],
#     4:[]

# }


# print(len(parking[1]))
# def ingresAuto():
#     valor=0
#     print("Ingresar vheiculo nuevo")
#     tipo=int(input("Que tipo es?: \n1.-Ligero\n2.-Mediano\n3.-Pesado"))
#     if tipo==1:
#         valor=2000
#     elif tipo==2:
#         valor=3000
#     elif tipo==3:
#         valor=3500
#     else:
#         print("Vehiculo invalido")
#     piso=int(input("EN que piso va?: "))
#     if piso in [1,2,3,4] and valor>0 :
#         if len(parking[piso])<10:
#             parking[piso].append(valor)
#             print("Agregado al piso", piso)
#         else:
#             print("Piso lleno")
#     else:
#         print("Piso no válido")
# def calculaGanancias():
#     totalGanancias=0
#     print("Contando Ganancias")
#     for piso in parking.values():
#         totalGanancias+=sum(piso)
#     print(f"El total recudado es {totalGanancias}")
# def cuentAutos():
#     totalAutos=0
#     for piso in parking.values():
#         totalAutos+=len(piso)
#     print("El total de autos en el parking es:", totalAutos)
# def muestrAutos():
#     for h, t in parking.items():
#         print(h, ".- ", t)

# def parkingAutos():
#     while True:
#         op=int(input("Seleccione un a opcion: "))
#         match op:
#             case 1:
#                 print("Ingresar vheiculo nuevo")
#                 tipo=int(input("Que tipo es?: \n1.-Ligero\n2.-Mediano\n3.-Pesado"))
#                 if tipo==1:
#                     valor=2000
#                 elif tipo==2:
#                     valor=3000
#                 elif tipo==3:
#                     valor=3500
#                 else:
#                     print("Vehiculo invalido")
#                 piso=int(input("EN que piso va?: "))
#                 if piso in [1,2,3,4]:
#                     if len(parking[piso])<10:
#                         parking[piso].append(valor)
#                         print("Agregado al piso", piso)
#                     else:
#                         print("Piso lleno")
#                 ingresAuto()
#             case 2:
#                 totalGanancias=0
#                 print("Contando Ganancias")
#                 for piso in parking.values():
#                     totalGanancias+=sum(piso)
#                 print(f"El total recudado es {totalGanancias}")
#                 calculaGanancias()
#             case 3:
#                 totalAutos=0
#                 for piso in parking.values():
#                     totalAutos+=len(piso)
#                 print("El total de autos en el parking es:", totalAutos)

                
#                 cuentAutos()
#             case 4:
#                 for h, t in parking.items():
#                     print(h, ".- ", t)
#                 muestrAutos()
#             case 5:
#                 print("Saliendo")
#                 break

        














