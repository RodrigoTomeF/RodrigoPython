#Funciones guia examen
 
 
 
autos = {
    'A001' : ['Toyota','Corolla',2010,5],
    'A002' : ['Ford', 'Ranger',2019,4],
    'A003' : ['Chevrolet', 'Spark',2022,4],
    'A004' : ['Suzuki', 'Aerio',2005,4],
    'A005' : ['Toyota','Yaris',2015,5],
    'A006' : ['Chevrolet', 'Impala',1950,1],
}
operaciones = {
    'A001' : ['01-01-2024','12-12-2025'],
    'A002' : ['07-08-2024','Pendiente'],
    'A003' : ['09-01-2025','Pendiente'],
    'A004' : ['24-03-2025','Pendiente'],
    'A005' : ['24-03-2024','24-07-2024'],
    'A006' : ['24-03-2024','24-09-2024'],
}

#buscar los datos de un auto por codigo
def buscarAuto(dic, busca):
    if busca in dic:
        print(dic[busca])
    else:
        print("El codigo del auto no existe")

car=input("Ingrese el codigo del auto a buscar: ")
buscarAuto(autos, car)

# def mostrar():
#     for i in autos:
#         print(f"{autos[i]}")


def mostrarautos(dic):
    for keys, values in (dic).items():
        print(f"{keys}.- {values}")


def ingresarauto():
    agregar_marca=input("Ingrese un auto: ")
    agregar_modelo=input("Ingresa el modelo: ")
    agrega_el_año=int(input("Ingresa el año del auto: "))
    agrega_el_ranking=float(input("Ingresa el ranking del auto: "))
    agregar_codigo=input("Ingrese el codigo: ")
    autos[agregar_codigo]=[agregar_marca, agregar_modelo, agrega_el_año, agrega_el_ranking]



ingresarauto()
mostrarautos(autos)


#guia para el examen 
#ejercicio 1


