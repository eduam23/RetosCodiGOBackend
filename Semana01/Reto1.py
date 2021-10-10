from datetime import datetime

print("=============================")
print("           Reto 1")
print("=============================")
nombre = input("Ingresa tu nombre: \n")
edad = int(input("Ingresa tu edad: \n"))
hora = int(datetime.now().strftime('%H'))

if(edad<18):
    if(hora>18 and hora<6):
        print("Debes de ir a dormir")
    else:
        print("Debes hacer tu tarea")
else:
    print("No estas obligado a hacer nada, pero puedes puedes aprovechar para estudiar Python 3")


