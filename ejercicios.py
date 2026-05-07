# número_a_multiplicar=int(input("Ingrese un número para multiplicar en la tabla: "))
# for i in range (número_a_multiplicar):
    
#     print(f"{número_a_multiplicar}X{i+1}={(1+i)*número_a_multiplicar}")


# número1=int(input("Ingrese el primer número: "))
# número2=int(input("Ingrese el segundo número:"))
# número3=int(input("Ingrese el tercer número: "))

# if (número1 >= número2) and (número1 >= número3):
#    largo = número1
# elif (número2 >= número1) and (número2 >= número3):
#    largo = número2
# else:
#    largo = número3

# print(f"El número más grande es {largo} ")

import random

número1=random.randint(1,7)
número2=random.randint(1,7)
número3=random.randint(1,7)
print(f"Número {número1}")
print(f"Número {número2}")
print(f"Número {número3}")

if (número1 >= número2) and (número1 >= número3):
   largo = número1
elif (número2 >= número1) and (número2 >= número3):
   largo = número2
else:
   largo = número3

print(f"El número más grande es {largo} ")


