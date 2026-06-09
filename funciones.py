# def saludo():
#     print("hola Lucash")
# n="Nano"
# print("Nos vemos", n)

# def chao():
#     print("Nos vemos", n)
# chao()


# def suma():


# número1=int(input("Ingrese un número: "))
# número2=int(input("Ingrese otro número: "))
# print(f"El resultado es {número1/número2}" )


#Una funcion sin argumento y sin retorno 

# def  saludame(name):
#     print("hola", name)

# saludame("Galon")

# def restalos(n1, n2):
#     print(f"El resultado de la resta es {n1-n2}")

# restalos(4,5)

# print("-"*30)

# print("Sin argumento y con retorno")

# def multiplica():
#     num1=8
#     num2=23
#     return num1*num2
# vari=multiplica()*4

# print(vari)

# print("-"*30)

# print ("con arguento y con retorno")

# def restalos(n1, n2):
#    return n1-n2 

# print(restalos(8, 9))


#Crea una calculadora, para ejecutar 
#Las operaciones basicas
#debe usar funciones con arumentos y retorno



# def calculadora():
#     while True:
#         try:
#             op=0
#             print("Calculadora")
#             print("1.- Suma")
#             print("2.- Resta")
#             print("3.- Multiplicación")
#             print("4.- División")
#             print("5.- Salir")

#             op=int(input("Ingrese la selección: "))

#             match op:
#                 case 1:
#                     num1=int(input("Ingrese un número: "))
#                     num2=int(input("Ingrese un segundo número: "))

#                     def suma(n1, n2):
#                         return n1 + n2
#                     print("Su suma es de sus números es de", suma(num1, num2))
#                     print("-"*30)
#                 case 2:
#                     num1=int(input("Ingrese un número: "))
#                     num2=int(input("Ingrese un segundo número: "))

#                     def resta(n1, n2):
#                         return n1 - n2
#                     print("Su resta es de sus números es de", resta(num1, num2))
#                     print("-"*30)

#                 case 3:
#                     num1=int(input("Ingrese un número: "))
#                     num2=int(input("Ingrese un segundo número: "))

#                     def Multiplicación(n1, n2):
#                         return n1 * n2
#                     print("Su multiplicación es de sus números es de", Multiplicación(num1, num2))
#                     print("-"*30)
#                 case 4:
#                     num1=int(input("Ingrese un número: "))
#                     num2=int(input("Ingrese un segundo número: "))

#                     def Division(n1, n2):
#                         return n1 / n2
#                     print("Su División es de sus números es de", Division(num1, num2))
#                     print("-"*30)

#                 case 5:
#                     print("-"*30)
#                     print("Usted esta saliendo de la calculadora")
#                     print("Gracias por usar el programa")
#                     break
                
#         except Exception as e:
#             print ("ERROR", e)


# calculadora()


#Crear un programa que calcule el IVA
#y retorne el valor con el IVA incluido 
#
#Usar argumento y retorno

# def Calcula_IVA(n1):
#     return n1 * 1,19

# print("-"*5, "Calcula el IVA", "-"*5)
# neto=int(input("Ingrese un número: "))

# print("El IVA calculado de su número es de", Calcula_IVA(neto))



