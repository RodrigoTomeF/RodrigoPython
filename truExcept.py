
#El try es para darle un aviso a una persona de poeque fallo

# while True:
#     try:
#         num=int(input("Ingrese un número: "))
#         break
#     except ValueError as er:
#         print("Error", er)
#         print("Solo debe ingresar números enteros")
#     else:
#         print("")


# op=0
# total=0
# while op!=4:
#     try:
#         print("1.- PC $500.000")
#         print("2.- LGTV 55 pulgadas $450.000")
#         print("3.- Microondas Mademsa $100.000")
#         print("4.- Salir")
#         print("Seleccione una opción")
#         op=int(input())
#     except ValueError as e:
#         print("Error", e)
#         print("Ingrese solo las opciones indicadas")
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





# peso_de_lata=int(input("Ingrese el peso de la lata: "))
# while peso_de_lata < 1:
#     print("Ingrese un número positivo")
#     peso_de_lata=int(input("Ingrese el peso de la lata otra vez: "))
# porcentaje_de_sodio=int(input("Ingrese el porcentaje de sodio: "))
# while porcentaje_de_sodio <= 1 | porcentaje_de_sodio >= 100:
#     print("Ingrese un número del 1 al 100")
#     porcentaje_de_sodio=int(input("Ingrese el porcentaje de sodio: "))
# try:
#     print("1.-Internacionalmente")
#     print("2.-Nacional")
#     venta=input("")
# except ValueError as e:
#     print("Error", e)
#     print("Ingrese una de las opciones permitidas")

# lata_normal_peso=500
# lata_mediana_peso=1500
# lata_grande_peso=9999

# if peso_de_lata <= lata_normal_peso:
#     tamaño_de_lata= "Lata normal"
# elif peso_de_lata <= lata_mediana_peso:
#     tamaño_de_lata= "Lata mediana"
# else:
#     tamaño_de_lata = "lata grande"

# lata_normal_sodio=5
# lata_especial_sodio=8
# lata_acorazada_sodio=100

# if porcentaje_de_sodio <= lata_normal_sodio:
#     lata_sodio = ""
# elif porcentaje_de_sodio <= lata_especial_sodio:
#     lata_sodio = "especial"
# else:
#     lata_sodio = "acorazada"

# opción1 = "Internacionalmente con stikcer sanitario"
# opcion2 = "Nacional sin sticker sanitario"
# if venta == opción1:
#     modo_de_venta = opción1
# else:
#     modo_de_venta = opcion2

# print(f"{tamaño_de_lata}, {lata_sodio}, {modo_de_venta}")

# while True:
#     try:
#         notas=int(input("Ingrese la cant de notas: "))
#     except:
#         print("Solo número enteros")

#     suma=0
#     for i in range(notas):
#         try:
#             n=float(input(f"Ingrese la nota {i+1}: "))
#             break
#         except:
#             print("Solo numeros decimales")
#         suma=suma+n
#     prom=suma/notas
#     print("El promedio es", round(prom,1))

#     if prom>=4:
#         print("Alumno aprobo")
#     else:
#         print("Alumno reprobo")






# Deberás construir un programa que esta diseñado para ayudar en la venta
# de pasajes. Inicia preguntándote cuántos pasajes deseas vender. Luego,
# utiliza un proceso organizado (llamado bucle for) para pedirte el precio de
# cada pasaje por separado. Si ingresas un valor que no es un número, te
# indica que necesitas proporcionar un valor numérico válido. Al final, muestra
# el monto total que se ha obtenido por la venta de todos los pasajes
# • Solicita al usuario la cantidad de pasajes a vender.
# • Se utiliza un bucle for para iterar sobre la cantidad de pasajes.
# • Dentro del bucle, se solicita al usuario el precio de cada pasaje y se
# acumula en la variable totalIngresos.
# • Si el usuario ingresa un valor no numérico para el precio del pasaje,
# el programa muestra un mensaje y sale del bucle usando break.
# • Finalmente, se imprime el total de ingresos por la venta de pasajes




# total_de_ingresos = 0
# while True:
#     try:
#         pasajes_a_vender = int(input("Ingrese la cantidad de pasajes a vender: "))
#         break
#     except:
#         print("Ingrese un valor númerico")
            
# for i in range(pasajes_a_vender):
#     print(f"¿Cuanto vale un boleto {i+1}: ?")
#     try:
#         precio_del_boleto=int(input(" "))
#         break
#     except:
#         print("Ingrese un valor númerico")
# total_de_ingresos = precio_del_boleto + pasajes_a_vender
# print(f"El total de dinero recaudado por las venta de los pasajes, es de {total_de_ingresos}")
    















