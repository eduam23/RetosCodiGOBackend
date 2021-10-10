import datetime

#variables
alumnos = []

def ConvertirFechaEnAño(strFecha):
    strFecha = int(strFecha[:4])
    return strFecha

#Entradas
cantidadAlumnos = int(input('¿Cuantos alumnos desea registrar? \n'))
for c in range(cantidadAlumnos):
    nombre = input('Ingrese Nombre: ')
    fechanac = input('Ingrese Fecha (Año-Mes-Día): ')
    alumno = [
        ConvertirFechaEnAño(fechanac), {
        'nombre':nombre,
        'fechanac': fechanac
        }
    ]
    alumnos.append(alumno)

alumnos.sort(reverse = True)

for a in alumnos:
    print(a)

