#ACTIVIDAD 4

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Usted es Niño/a")
elif edad >= 12 and edad < 18:
    print("Usted es adolecente")
elif edad >= 18 and edad < 30:
    print("Usted es adulto/a joven")
else:
    print("Usted es adulto/a")             