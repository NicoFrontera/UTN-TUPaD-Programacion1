#EJERCICIO 2

usuario_correcto = "alumno"
clave_correcto = "python123"

intentos = 0
acceso_concedido = False

while intentos < 3:
    print(f"Intento {intentos+1}/3 - Usuario:", end=" ")
    usuario = input()
    clave = input("Clave: ")

    if usuario == usuario_correcto and clave == clave_correcto:
        print("Acceso concedido.")
        acceso_concedido = True
        break
    else:
        print("Error: credenciales inválidas.")
        intentos += 1

if not acceso_concedido:
    print("Cuenta bloqueada.")
else:
    while True:
        print("\n1) Estado   2) Cambiar clave   3) Mensaje   4) Salir")
        opcion = input("Opción: ")

        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
            continue

        opcion = int(opcion)

        if opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango.")
            continue

        if opcion == 1:
            print("Inscripto")

        elif opcion == 2:
            nueva = input("Nueva clave: ")
            if len(nueva) < 6:
                print("Error: la clave debe tener mínimo 6 caracteres.")
                continue

            confirm = input("Confirmar nueva clave: ")

            if nueva == confirm:
                clave_correcta = nueva
                print("Clave actualizada con exito.")
            else:
                print("Error: las claves no coinciden.")

        elif opcion == 3:
            print("Segui adelante, vas bien!")

        elif opcion == 4:
            print("Saliendo del sistema.")
            break