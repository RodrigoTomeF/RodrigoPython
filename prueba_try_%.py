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
# EJ: Hay 4 indies, y 5 de estudio, sol 3 son clasificacion e
Indie=0
estudios=0
edad=0
clasificaión_e=0
while True:
    try:
        cantidad_juegos = int(input("¿Cuántos juegos vas a registrar?: "))
        if cantidad_juegos > 0:
            break
        print("Por favor, ingresa un número mayor a 0")
    except ValueError:
        print("Debes ingresar un número entero")

while True:
    nombre_del_juego = input("Ingrese el nombre del juego: ").upper()
    if len(nombre_del_juego) < 5:
        print("Su nombre debe tener al menos 5 letras ")
    elif " " in nombre_del_juego:
        print("Su nombre no debe de tener espacios ")
    else:
        break

while True:
    try:
        Precio=int(input("Ingrese el precio: "))
        if Precio > 0:
            break
        print("Coloque un valor positivo")
    except ValueError:
        print("Debe colocar un número sobre 0")

if 20000 < Precio < 40000:
    Indie =+ 1
elif Precio >= 40000:
    estudios =+ 1

while True:
    try:
        edad=int(input("Ingrese la edad: "))
        if edad >= 0:
            break
        print("La edad debe ser un valor positivo")
    except ValueError:
        print("Debe colocar un número sobre 0")

if edad <= 12:
    clasificaión_e += 1 
    print("La clasificación es E")
elif 12 <= edad <= 17:
    print("La clasificación es para adolecente")
else:
    print("Su claificacion es para +18")

print(f"Hay {Indie} indies, y {estudios} estudios, son {clasificaión_e} son clasificaciones E ")



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

deuda=100000
cupo_disponible=500000
opcion=0
while True:
    print("Menu tarjeta de credito")
    print(f"Saldo de tarjeta ${cupo_disponible} ")
    print(f"Dueda a pagar ${deuda} ")
    print("1- Pago de la tarjeta de crédito")
    print("2- Smulación de compra")
    print("3- Salir")


    try:
        print("Elija una de las opcines de arriba")
        opcion=int(input(""))
        match opcion:
            case 1:
                print("Pago a la tarjeta de credíto")
                try:
                    pago=int(input("Ingresa un monto a pagar: "))
                    if pago < 0:
                        print("El monto no debe ser menor a 0")
                    elif pago > deuda:
                        print("Usted no puede pagar más de lo que debe de deuda")
                    else:
                        deuda = deuda - pago
                        print(f"Su nueva deuda es de ${deuda}")
                except ValueError:
                    print("Debe agregar un valor numerico")
            case 2:
                try:
                    print("Simulación de compra ")

                    monto_de_compra=int(input("Ingresa el monto a comprar"))
                    if monto_de_compra <= 0:
                        print("Su compra no puede ser negativo")
                    elif monto_de_compra >= cupo_disponible:
                        print("No tienes el cupo suficiente para gastar")
                    else:
                        cupo_disponible = cupo_disponible - monto_de_compra
                        deuda = deuda + monto_de_compra
                        print(f"Su compra fue exitosa, su nueva deuda es de ${deuda}")
                except ValueError:
                    print("Debes ingresar un valor númerico")
            case 3:
                print("Gracias por usar el sistema, bye")
                break
    except ValueError:
        print("Solo un numero del 1 al 3")