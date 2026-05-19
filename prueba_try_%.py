# registro de juegos
# preguntar cuantos juegos son, 
# Debe preguntar al usuario Nombre del juego;
# -Al menos 5 caracteres 
# -No debe incluir espacios y todas mayusculas
# preguntar precio
# -Solo numeros enteros positivos 
# -si vale mas de 20000 es Indie pero menos de 40000
# -Si vale 40000 o mas, es de estudio 
# -mostrar al final cuantos hay de cada categoria
# clasificacion
# - E para todos (<12)
# - +12 para adolecentes (12 y 17)
# -M para personas de mas de 18 (+18)
# - Mostrar resumen 
# EJ: Hay 4 indies, y 5 de estudio, sol 3 son clasificacion E



# Precio_del_juego=0

# Cantidad_de_juegos=int(input("Ingrese la cantidad de juegos: "))


# Nombre_del_juego=input("Ingrese el nombre del juego: ")


# Precio_del_juego=int(input("Ingresa el precio del juego: "))


# Juego_indie=0 or 20000 or 39999

# if Precio_del_juego >= Juego_indie:
    
# elif Precio_del_juego <= 40000:
#     print()


# El programa debe tener un menú de opciones de donde se pueda
#  realizar el pago del cupo de la tarjeta de crédito, como también simular
#  nuevas compras, y estas una vez sumadas se resten al cupo disponible. 
# Las opciones disponibles deben estar construidas de la siguiente forma:
# 1.	Pago de Tarjeta de Crédito:
# a.	El usuario comienza con una deuda de $100.000
# b.	El usuario puede ingresar un monto para realizar un pago en la tarjeta de crédito.
# c.	Se debe verificar que el monto ingresado sea mayor o igual a cero.
# d.	Se debe verificar que el monto a pagar no exceda el saldo actual de la tarjeta.
# e.	Al pagar el sistema debe descontar de la deuda total
# f.	Si las verificaciones son exitosas, se realiza el pago y se actualiza el saldo de la tarjeta.
# 2.	Simulación de Compras:
# a.	El usuario puede simular realizar un número ilimitado de compras.
# b.	Para cada compra, se solicita al usuario ingresar el monto de la compra. El programa suma los montos de cada compra. 
# c.	Se verifica que el monto de la compra sea mayor o igual a cero.
# d.	Se realiza la compra y se actualiza el saldo de la tarjeta para cada iteración del bucle for.
# 3.	Salir:
# a.	Al seleccionar esta opción, el programa debe cerrarse o finalizar.

# A considerar:
# 1.	Manejo de Errores:
# a.	Se utilizan bloques try y except para manejar posibles errores al ingresar datos, validar valores no numéricos y errores inesperados. 
# b.	Se debe programar mensajes de error específicos para guiar al usuario sobre posibles problemas.


Tarjeta_cupo=100.000

monto_de_pago=int(input("Ingresa un monto en en la tarjeta: "))

if monto_de_pago >= 0 and monto_de_pago <=100.000:
    print(f"Usted ingreso {monto_de_pago}")
    Tarjeta_cupo=Tarjeta_cupo
if monto_de_pago >= 100000:
    print("Usted se paso del número permitido")

if monto_de_pago > Tarjeta_cupo:
    print("Usted excedio el limite de la tarjeta")
 






























