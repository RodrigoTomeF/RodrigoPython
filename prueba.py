# # print("ingrese nombre")
# # nombre=input()
# # edad=int(print("ingrese su edad: ", ))

# # print("hola", nombre, "su edad en 5 años será", edad+5)

# n1=int(print("Ingrese un número: "))
# n2=int(print("Ingrese otro número: "))
# resultados_suma=n1+n2
# resultados_resta=n1-n2
# print("El resultado de la suma es", resultados_suma) 
# print("El resultdo de la resta es", resultados_resta)

#calcular el iva para cada compra
print(
'''
1.- pera 1200
2.- manzana 1400
3.- piña 2000
''')

select=int(input("seleccione una fruta: "))
if select==1:
    print("El total a pagar", 1200*1.19)
elif select==2:
    print("El total a pagar", 1400*1.19)
elif select==3:
    print("El total a pagar", 2000*1.19)
else:
    print("número no valido")
