# op=0
# total=0
# while op!=4:
#     print("1.- PC $500.000")
#     print("2.- LGTV 55 pulgadas $450.000")
#     print("3.- Microondas Mademsa $100.000")
#     print("4.- Salir")
#     print("Seleccione una opcion")
#     op=int(input())
#     match op:
#         case 1: 
#             print("El total a pagar es ",500000*1.19)
#             total+=500000*1.19
#         case 2:
#             print("El total a pagar es ",450000*1.19)
#             total+=450000*1.19
#         case 3:
#             print("El total a pagar es ",100000*1.19)
#             total+=100000*1.19
#         case 4:
#             print("Saliendo")
#             print("El total a pagar es", total)
#         case _:
#             print("Seleccion invalida")






# op=0
# while op!=5:
#     print("1.- Suma")
#     print("2.- Resta")
#     print("3.- Multiplicar")
#     print("4.- Dividir")
#     print("5.- Salir")
#     print("seleccione una opción")
#     op=int(input())
#     match op:
#         case 1:
#             número1=int(input("Ingrese un número: "))
#             número2=int(input("Ingrese otro número: "))
#             print(f"El resultado es {número1+número2}" )
#         case 2:
#             número1=int(input("Ingrese un número: "))
#             número2=int(input("Ingrese otro número: "))
#             print(f"El resultado es {número1-número2}" )
#         case 3:
#             número1=int(input("Ingrese un número: "))
#             número2=int(input("Ingrese otro número: "))
#             print(f"El resultado es {número1*número2}" )
#         case 4:
#             número1=int(input("Ingrese un número: "))
#             número2=int(input("Ingrese otro número: "))
#             print(f"El resultado es {número1/número2}" )
#         case 5:
#             print("Saliendo")
#         case _:
#             print("Selección invalida")


# def suma():
#  número1=int(input("Ingrese un número: "))
#  número2=int(input("Ingrese otro número: "))
#  print(f"El resultado es {número1+número2}" )

# def resta():
#  número1=int(input("Ingrese un número: "))
#  número2=int(input("Ingrese otro número: "))
#  print(f"El resultado es {número1-número2}" )

# def multiplicar():
#  número1=int(input("Ingrese un número: "))
#  número2=int(input("Ingrese otro número: "))
#  print(f"El resultado es {número1*número2}" )

# def dividir():
#  número1=int(input("Ingrese un número: "))
#  número2=int(input("Ingrese otro número: "))
#  print(f"El resultado es {número1/número2}" )

# def calculadora():
#     op=0
#     while op!=5:
#         print("1.- Suma")
#         print("2.- Resta")
#         print("3.- Multiplicar")
#         print("4.- Dividir")
#         print("5.- Salir")
#         print("seleccione una opción")
#         op=int(input())
#         match op:
#             case 1:
#                 suma()
#             case 2:
#                 resta()
#             case 3:
#                 multiplicar()
#             case 4:
#                 dividir()
#             case 5:
#                 print("Saliendo")
#             case _:
#                 print("Selección invalida")


# def Tabla_de_multiplicar():
#    num=int(input("Ingresa un número: "))
#    for i in range (10):
#     print( num, "X", i+1, "=", num*(i+1))

# def Compra_de_frutas():
#     ('''
#     1.- pera 1200
#     2.- manzana 1400
#     3.- piña 2000
#     ''')

#     select=int(input("seleccione una fruta: "))
#     if select==1:
#         print("El total a pagar", 1200*1.19)
#     elif select==2:
#         print("El total a pagar", 1400*1.19)
#     elif select==3:
#         print("El total a pagar", 2000*1.19)
#     else:
#         print("número no valido")


# def Calcula_tu_edad_en_unos_5_años():
#     print("ingrese nombre")
#     nombre=input()
#     edad=int(print("ingrese su edad: ", ))

#     print("hola", nombre, "su edad en 5 años será", edad+5)

# def programas():
#     op=0
#     while op!=4:
#         print("1.- Tabla de multiplicar")
#         print("2.- Compra de frutas")
#         print("3.- Calcula tu edad en 5 años")
#         print("4.- Salir")
#         print("seleccione una opción")
#         op=int(input())
#         match op:
#             case 1:
#                 Tabla_de_multiplicar()
#             case 2:
#                 Compra_de_frutas()
#             case 3:
#                 Calcula_tu_edad_en_unos_5_años()
#             case 4:
#                 print("Saliendo")
#             case _:
#                 print("Seleccion inválida")