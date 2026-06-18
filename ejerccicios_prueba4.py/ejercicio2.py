#crear un gestor de pacientes


#Crear al gestor de pacientes en un centro medico
#para poner el nombre se debe validar que no este vacio
#y ademas tenga mas de 8 caracteres
#para la prevision de salud solo existen 3 posibles valores
#fonas, isapre, o fodesa
#Al ingresar un paciente, se debe poner la temperatura
#crear una funcion que valide si esta grave o no
#para que este grave debe tener mas de 39


pacientes=[
    {"nombre": "Aquiles Baeza", 
    "prevision": "fonasa", "temperatura":34.6, "grave": False}
]

def mostrar_prevision():
    print("fonasa")
    print("isapre")
    print("fodesa")

temperatura_del_paciente=0
 
print("-"*40)
print("gestor de pacientes")
nombre_del_paciente=input("Ingrese nombre del paciente: ")
while nombre_del_paciente == "" or len(nombre_del_paciente) <=8:
    print("ERROR, el nombre no puede tener 0 caracteres, ni menos de 8")
    nombre_del_paciente=input("Ingrese nombre del paciente: ")

mostrar_prevision()
prevision_del_paceinte=input("Ingrese la prevision de su uso: ").lower()
while prevision_del_paceinte not in ["fonasa","isapre", "fodesa"]:
    mostrar_prevision()
    print("ERROR, debe elegir una de las opciones")
    prevision_del_paceinte=input("Ingrese la prevision de su uso: ").lower()

temperatura_del_paciente=float(input("Ingrese la temperatura del paciente: s"))
if temperatura_del_paciente >= 39:
    grave = True
else:
    grave = False

pacientes.append({"nombre":nombre_del_paciente, "prevision":prevision_del_paceinte, "temperatura":temperatura_del_paciente, "grave":grave})

