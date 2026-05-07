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



peso_de_lata=int(input("Ingrese el peso de la lata: "))
while peso_de_lata < 1:
    print("Ingrese un número positivo")
    peso_de_lata=int(input("Ingrese el peso de la lata otra vez: "))
porcentaje_de_sodio=int(input("Ingrese el porcentaje de sodio: "))
while porcentaje_de_sodio <= 1 | porcentaje_de_sodio >= 100:
    print("Ingrese un número del 1 al 100")
    porcentaje_de_sodio=int(input("Ingrese el porcentaje de sodio: "))
print("1.-Internacionalmente")
print("2.-Nacional")
venta=input("")

lata_normal_peso=500
lata_mediana_peso=1500
lata_grande_peso=9999

if peso_de_lata <= lata_normal_peso:
    tamaño_de_lata= "Lata normal"
elif peso_de_lata <= lata_mediana_peso:
    tamaño_de_lata= "Lata mediana"
else:
    tamaño_de_lata = "lata grande"

lata_normal_sodio=5
lata_especial_sodio=8
lata_acorazada_sodio=100

if porcentaje_de_sodio <= lata_normal_sodio:
    lata_sodio = ""
elif porcentaje_de_sodio <= lata_especial_sodio:
    lata_sodio = "especial"
else:
    lata_sodio = "acorazada"

opción1 = "Internacionalmente con stikcer sanitario"
opcion2 = "Nacional sin sticker sanitario"
if venta == opción1:
    modo_de_venta = opción1
else:
    modo_de_venta = opcion2

print(f"{tamaño_de_lata}, {lata_sodio}, {modo_de_venta}")



# # número_a_multiplicar=int(input("Ingrese un número para multiplicar en la tabla: "))
# # for i in range (número_a_multiplicar):
    
# #     print(f"{número_a_multiplicar}X{i+1}={(1+i)*número_a_multiplicar}")


# # número1=int(input("Ingrese el primer número: "))
# # número2=int(input("Ingrese el segundo número:"))
# # número3=int(input("Ingrese el tercer número: "))

# # if (número1 >= número2) and (número1 >= número3):
# #    largo = número1
# # elif (número2 >= número1) and (número2 >= número3):
# #    largo = número2
# # else:
# #    largo = número3

# # print(f"El número más grande es {largo} ")

# import random

# número1=random.randint(1,7)
# número2=random.randint(1,7)
# número3=random.randint(1,7)
# print(f"Número {número1}")
# print(f"Número {número2}")
# print(f"Número {número3}")

# if (número1 >= número2) and (número1 >= número3):
#    largo = número1
# elif (número2 >= número1) and (número2 >= número3):
#    largo = número2
# else:
#    largo = número3

# print(f"El número más grande es {largo} ")

