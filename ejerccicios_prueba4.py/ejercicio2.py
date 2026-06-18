#crear un gestor de pacientes


#Crear al gestor de pacientes en un centro medico
#para poner el nombre se debe validar que no este vacio
#y ademas tenga mas de 8 caracteres
#para la prevision de salud solo existen 3 posibles valores
#fonas, isapre, o fodesa
#Al ingresar un paciente, se debe poner la temperatura
#crear una funcion que valide si esta grave o no
#para que este grave debe tener mas de 39


# pacientes=[
#     {"nombre": "Aquiles Baeza", 
#     "prevision": "fonasa", "temperatura":34.6, "grave": False}
# ]

# def mostrar_prevision():
#     print("fonasa")
#     print("isapre")
#     print("fodesa")

# temperatura_del_paciente=0
 
# print("-"*40)
# print("gestor de pacientes")
# nombre_del_paciente=input("Ingrese nombre del paciente: ")
# while nombre_del_paciente == "" or len(nombre_del_paciente) <=8:
#     print("ERROR, el nombre no puede tener 0 caracteres, ni menos de 8")
#     nombre_del_paciente=input("Ingrese nombre del paciente: ")

# mostrar_prevision()
# prevision_del_paceinte=input("Ingrese la prevision de su uso: ").lower()
# while prevision_del_paceinte not in ["fonasa","isapre", "fodesa"]:
#     mostrar_prevision()
#     print("ERROR, debe elegir una de las opciones")
#     prevision_del_paceinte=input("Ingrese la prevision de su uso: ").lower()

# temperatura_del_paciente=float(input("Ingrese la temperatura del paciente: s"))
# if temperatura_del_paciente >= 39:
#     grave = True
# else:
#     grave = False

# pacientes.append({"nombre":nombre_del_paciente, "prevision":prevision_del_paceinte, "temperatura":temperatura_del_paciente, "grave":grave})





pacientes=[
    {"nombre": " Aquiles Baeza", "prevision": "Fonasa", 
     "temperatura":34.6, "grave": False}
]

'''crear al gestor de pacientes en un centro medico
Para poner el nombre se debe validar que no este vacio 
y ademas tenga mas de 8 caracteres
Para la prevision de salud solo exiten 3 posibles valores
Fonasa, Isapre, o Fodesa
Al ingresar un paciente, se debe poner la temperatura
Crear una funcion que valide si esta grave o no
Para que este grave debe tener mas de 39°
Cada atencion vale $25.000
Los despcuentos corresponden a 
FOnasa 54%
Isapre 27%
Fodesa 12,5%

'''
def ingresarpaciente():
    print("-"*30)
    nombre=input("Ingrese nombre: ")
    while nombre == "" or len(nombre)<=8:
        print("ERROR. Debe agregar un nombre que tenga mas de 8 letras.")
        nombre=input("Ingrese nombre: ")
    mostrar_prevision()
    prevision=int(input("Ingrese prevision: ")).lower()
    while prevision not in ["fonasa", "isapre", "fodesa"]:
        print("Debe elegir una de las opciones disponibles")
        prevision=input("Ingrese prevision: ").lower()
    temp=float(input("Ingrese temp: "))
    pacientes.append({"nombre": nombre, "prevision": prevision, 
                "temperatura":temp, "grave": validarEstado(temp)})
    print("Paciente agregado al listado")

def mostrar_prevision():
    print("1.- fonasa")
    print("2.- isapre")
    print("3.- fodesa")

def validarEstado(tempe):
   if tempe>39:
       return True 
   else:
       return False
def mostrarPacientes():
    if len(pacientes)==0:
        print("No hay pacientes")
    else:
        c=1
        for p in pacientes:
            print(f"{c} .- {p}")
            c+=1
while True:
    try:
        print("1.- Ingresar paciente")
        print("2.- Quitar paciente")
        print("3.- Tomar Temperatura")
        print("4.- Cobra atencion")
        print("5.- Mostrar Pacientes")
        print("9.- Salir")
        op=int(input("Ingrese una opcion: "))
        match op:
            case 1:
                ingresarpaciente()
            case 2:
                mostrarPacientes()
                paci=int(input("Que paciente se vá?: "))
                pacientes.pop(paci-1)
                print("Paciente eliminado.")
            case 3:
                print("")
            case 4:
                print("")
            case 5:
                mostrarPacientes()
            case 9:
                print("Saliendo")
                break
            case _:
                print("Opción inválida")
    except Exception as e:
        print("Error:" , e)