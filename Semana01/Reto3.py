class Productos:
    def __init__(self,nom,des):
        self.nombre = nom
        self.descripcion = des
    
    def mostrar(self, contador):
        print( str(contador) + ". "+ self.nombre)

productos = []
opcion = ''

print("\n")
print("=====================================")
print("        REGISTRO DE PRODUCTOS")
print("=====================================\n")

while(opcion != 4):
    opcion = int(input("OPCIONES: \n 1.Registrar \n 2.Mostrar \n 3.Seleccionar \n 4.Salir \n"))
    if(opcion != 4):
        if(opcion == 1):
            nombre = input("\nIngresa el nombre del producto : \n")
            descripcion = input("Ingresa la descripcion del producto : \n")
            producto = Productos(nombre,descripcion)
            productos.append(producto)
        if(opcion == 2):
            contador = 1
            print('\nUtiliza el indice en la opción "Seleccionar"')
            for a in productos:
                a.mostrar(contador)
                contador += 1
        if(opcion == 3):
            indice = int(input("\nIngrese el indice del producto:\n"))
            indice-=1
            print("\nNombre del producto: " + productos[indice].nombre)
            print("Descripción del producto: " + productos[indice].descripcion + "\n")
        else:
            print("") 

print("\n¡Has terminado el programa!")