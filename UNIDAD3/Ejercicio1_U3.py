#EJERCICIO 1

nombre = input("Ingrese el nombre del cliente: ")

while not nombre.isalpha():
    print("Error: el nombre debe contener solo letras.")
    nombre = input("Ingrese el nombre del cliente: ")

cant_productos = input("Ingrese la cantidad de productos a comprar: ")

while not cant_productos.isdigit() or int(cant_productos) <= 0:
    print("Error: la cantidad tiene que ser numero positivo mayor a 0")
    nombre = input("Ingrese la cantidad de productos a comprar: ")

cant_productos = int(cant_productos)    

total_sin_descuento = 0
total_con_descuento = 0

for i in range(1,cant_productos+1):
    print(f"Producto {i}")
    precio = input("Precio: ")
    while not precio.isdigit():
        print("Error: Ingrese un numero entero valido: ")
        precio = input("Precio:")
    precio = int(precio)

    descuento = input("El producto tiene descuento? (S/N)")
    while descuento.upper() not in ("S", "N"):
        print("Error: Ingrese S o N.")
        descuento = input("El producto tiene descuento? (S/N)")

    total_sin_descuento += precio

    if descuento.upper() == "S":
        precio_con_descuento = precio * 0.90
    else:
        precio_con_descuento = precio

    total_con_descuento += precio_con_descuento

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cant_productos

print(f"\nCliente: {nombre}")
print(f"Total sin descuentos: ${total_sin_descuento}")
print(f"Total con descuentos: ${total_con_descuento}")
print(f"Ahorro: ${ahorro: .2f}")
print(f"Promedio por producto: ${promedio: .2f}")