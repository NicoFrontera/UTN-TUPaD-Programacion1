#ACTIVIDAD 8

nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese 1 para mayusculas, 2 para minusculas o 3 para la primera letra en mayuscula: "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Invalido")

