# #Uso y ejemplo de random

import random
# # dado=random.randint(1,10)  #Int por que es un número entero.
# # print(dado)

# # for i in range(dado):
# #     print("Hola deny")

# dado1=random.randint(1,10)

# dado2=random.randint(1,10)


# print(f"El dado 1 dio {dado1}") 
# print(f"El dado 2 dio {dado2}")

# if dado1==dado2:
#     print("Se va a la carsel")
# else:
#     print("Avance por favor")


# import random
# Contador=0
# resultado_del_número_random=random.randint(1,100)
# Adivinansa_del_usuario=print(input("Ingrese un número para adivinar entre 1 y 100 "))

# while Contador >= 5:

#     if Adivinansa_del_usuario > resultado_del_número_random:
#         print("Te pasaste")
#     else:
#         print("El número a adivinar es mayor")

# import random

# print("Intenta adivinar un número")

# num=random.randint(1,100)
# intentos=5
# while intentos > 0:
#     adivina=int(input("Ingresa un número del 1 al 100:"))
#     print("")
# import time
# hp1=100
# hp2=100
# player1=input("Ingresa al primer luchador:")
# player2=input("Ingresa al segundo luchador:")


# while hp1 > 2 and hp2 > 2:
#     turno=random.randint(1,2)
#     if turno %2==0:
#         golpe=random.randint(7,18)
#         hp2=hp2-golpe
#         print(f"El luchador {player1} golpea al luchador {player2}")
#         print(f"El luchador {player2} le quedan {hp2} de vida")
#     else:
#         golpe=random.randint(7,18)
#         hp1=hp1-golpe
#         print(f"El luchador {player2} golpea al luchador {player1}")
#         print(f"El luchador {player1} le quedan {hp1} de vida")
#     time.sleep(2)
# if hp1 <= 2:
#     print(f"El jugador {player1} a perdido")
    






# j1=random.randint(60,190)
# j2=random.randint(60,190)
# j3=random.randint(60,190)
# print(f"El jugador 1 lanzo la pelota {j1} metros")
# print(f"El jugador 2 lanzo la pelota {j2} metros")
# print(f"El jugador 3 lanzo la pelota {j3} metros")

# if j1>j2 and j1>j3:
#     print("El jugador 1, lanzo la pelota más lejos")
# elif j2>j3:
#     print("El jugador 2, lanzo la pelota más lejos")
# else:
#     print("El jugador 3, lanzo la pelota más lejos")


#ponerle un imite al usuario a la hora de escribir en un print

import time 


# lanzamiento1=random.randint(1,9)
# lanzamiento2=random.randint(1,9)
# lanzamiento3=random.randint(1,9)
# numero_adivi1=3
# numero_adivi2=7
# numero_adivi3=2
# while True:
#     print(f"Primer lanzamiento sale {lanzamiento1} y el núnmero a adivinar es {numero_adivi1}")
#     if lanzamiento1 == numero_adivi1:
#         print("El primer número es correcto")
#     else:
#         print("El primer número no es correcto")

#     print(f"Primer lanzamiento sale {lanzamiento2} y el núnmero a adivinar es {numero_adivi2}")
#     if lanzamiento2 == numero_adivi2:
#         print("El primer número es correcto")
#     else:
#         print("El primer número no es correcto")


#     print(f"Primer lanzamiento sale {lanzamiento3} y el núnmero a adivinar es {numero_adivi3}")
#     if lanzamiento1 == numero_adivi3:
#         print("El primer número es correcto")
#     else:
#         print("El primer número no es correcto")

#     time.sleep(2)


# lanzamiento1=random.randint(1,9)
# lanzamiento2=random.randint(1,9)
# lanzamiento3=random.randint(1,9)
# t1=False
# t2=False
# t3=False
# nums=0
# print(f"Los numeros generados son: {lanzamiento1}, {lanzamiento2}, {lanzamiento3}")
# while not t1 or not t2 or not t3:
#     numerito=random.randint(1,9)
#     print("El numero es", numerito)
#     time.sleep(1)
#     if numerito==lanzamiento1(1,9):
#         t1=True
#     if numerito==lanzamiento2(1,9):
#         t2=True
#     if numerito==lanzamiento3(1,9):
#         t3=True
#     nums+=1
# print(f"GANASTE, en {nums} turnos")


'''
Fabrica de enlatados
Se necestita hacer el algoritmo de productos enlatados
se debe consultar el peso del producto (en gramos) (solo valores positivos)
El porcentaje de sodio en el (solo valores entre 1 y 100)
y si se va a vender nacional o internacionalmente
considerar los criterios en la siguiente tabla 

menos de 500 grs, lata normal
501 hasta 1500 grs, lata mediana
1501 y más, lata grande.
si el sodio es menos de 5%, lata queda igual 
si e entre 5% y 8% lata especial
si tienes 9% o más, lata acorazada
a las latas internacionales, se le debe pegar 
un sticker de validació sanitaria 

el:800, 7%, lima==> lata mediana especial con sticker sanitario
'''



peso_del_producto=int(input("Ingrese el peso del producto: "))
porcentaje_de_sodio=int(input("Ingrese el porcentaje de sodio: "))
Lata_envio=int(input("Envio internacional ?: "))


if peso_del_producto <= 500:
    tipo_de_lata="lata pequeña"
elif peso_del_producto <= 1500:
    tipo_de_lata= "lata mediana"
else:
    tipo_de_lata= "lata grande"

if porcentaje_de_sodio <= 5:
    porcentaje=""
elif porcentaje_de_sodio <= 8: 
    porcentaje="especial"
else: 
    print("usted eligio la lata acorazada")
    porcentaje="acorazado"

if Lata_envio == "internacional":
    envio="con stiker sanitario"

print(f"Lata {tipo_de_lata} {porcentaje} {envio}")


# while peso_del_producto<1:
#     print("Ingrese solo valores positivos")
#     peso_del_producto=int(input("Ingrese el porcentaje de sodio del producto: "))

