#EJERCICIO 3

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

operador = input("Ingrese el nombre del operador: ")

while not operador.isalpha():
    print("Error: Debe ingresar solo letras.")
    operador = input("\nIngrese el nombre del operador: ")

opcion = 0

while opcion != 5:
    print("MENU PRINCIPAL")
    print("1. Reservar turno")
    print("2. Cancelar turno")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    opcion = input("Seleccione una opcion: ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 5:
        print("Error: opción inválida.")
        opcion = input("Seleccione una opcion: ")

    opcion = int(opcion)

    if opcion == 1:
        print("Reservar turno")
        dia = input("Seleccione 1 (Lunes) o 2 (Martes): ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: Dia invalido.")
            dia = input("Seleccione 1 (Lunes) o 2 (Martes): ")

        dia = int(dia)

        nombre_paciente = input("Ingrese el nombre del paciente: ")

        while not nombre_paciente.isalpha():
            print("Error: Nombre invalido.")
            nombre_paciente = input("Ingrese el nombre del paciente: ")

        if dia == 1:

            turno = (
                nombre_paciente == lunes1 or
                nombre_paciente == lunes2 or
                nombre_paciente == lunes3 or
                nombre_paciente == lunes4
            )

            if turno:
                print("El paciente ya tiene turno el lunes.")
            else:
                if lunes1 == "":
                    lunes1 = nombre_paciente
                    print("Turno reservado en Lunes 1.")
                elif lunes2 == "":
                    lunes2 = nombre_paciente
                    print("Turno reservado en Lunes 2.")
                elif lunes3 == "":
                    lunes3 = nombre_paciente
                    print("Turno reservado en Lunes 3.")
                elif lunes4 == "":
                    lunes4 = nombre_paciente
                    print("Turno reservado en Lunes 4.")
                else:
                    print("No hay turnos disponibles el lunes.")

        else:
            turno = (
                nombre_paciente == martes1 or
                nombre_paciente == martes2 or
                nombre_paciente == martes3
            )

            if turno:
                print("El paciente ya tiene turno el martes.")
            else:
                if martes1 == "":
                    martes1 = nombre_paciente
                    print("Turno reservado en Martes 1.")
                elif martes2 == "":
                    martes2 = nombre_paciente
                    print("Turno reservado en Martes 2.")
                elif martes3 == "":
                    martes3 = nombre_paciente
                    print("Turno reservado en Martes 3.")
                else:
                    print("No hay turnos disponibles el martes.")

    elif opcion == 2:
        print("Cancelar turno.")
        dia = input("Seleccione 1 (Lunes) o 2 (Martes): ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: Dia invalido.")
            dia = input("Seleccione 1 (Lunes) o 2 (Martes): ")

        dia = int(dia)

        nombre_paciente = input("Ingrese el nombre del paciente a cancelar: ")

        while not nombre_paciente.isalpha():
            print("Error: Nombre invalido.")
            nombre_paciente = input("Ingrese el nombre del paciente a cancelar: ")

        turno_encontrado = False

        if dia == 1:
            if lunes1 == nombre_paciente:
                lunes1 = ""
                turno_encontrado = True
            elif lunes2 == nombre_paciente:
                lunes2 = ""
                turno_encontrado = True
            elif lunes3 == nombre_paciente:
                lunes3 = ""
                turno_encontrado = True
            elif lunes4 == nombre_paciente:
                lunes4 = ""
                turno_encontrado = True

        else:
            if martes1 == nombre_paciente:
                martes1 = ""
                turno_encontrado = True
            elif martes2 == nombre_paciente:
                martes2 = ""
                turno_encontrado = True
            elif martes3 == nombre_paciente:
                martes3 = ""
                turno_encontrado = True

        if turno_encontrado:
            print("\nTurno cancelado con exito.")
        else:
            print("\nNo se encontro ese turno.")

    elif opcion == 3:
        print("Ver agenda del dia.")
        dia = input("Seleccione 1 (Lunes) o 2 (Martes): ")

        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            print("Error: Dia invalido.")
            dia = input("Seleccione 1 (Lunes) o 2 (Martes): ")

        dia = int(dia)

        if dia == 1:
            print("AGENDA LUNES:")
            print("1.", lunes1 if lunes1 != "" else "(libre)")
            print("2.", lunes2 if lunes2 != "" else "(libre)")
            print("3.", lunes3 if lunes3 != "" else "(libre)")
            print("4.", lunes4 if lunes4 != "" else "(libre)")
        else:
            print("AGENDA MARTES:")
            print("1.", martes1 if martes1 != "" else "(libre)")
            print("2.", martes2 if martes2 != "" else "(libre)")
            print("3.", martes3 if martes3 != "" else "(libre)")

    elif opcion == 4:
        print("Resumen general")

        ocupados_lunes = (lunes1 != "") + (lunes2 != "") + (lunes3 != "") + (lunes4 != "")
        ocupados_martes = (martes1 != "") + (martes2 != "") + (martes3 != "")

        libres_lunes = 4 - ocupados_lunes
        libres_martes = 3 - ocupados_martes

        print("Lunes:", ocupados_lunes, "ocupados /", libres_lunes, "libres")
        print("Martes:", ocupados_martes, "ocupados /", libres_martes, "libres")

        if ocupados_lunes > ocupados_martes:
            print("El dia con más turnos ocupados es LUNES.")
        elif ocupados_martes > ocupados_lunes:
            print("El dia con más turnos ocupados es MARTES.")
        else:
            print("Hay empate")

print("Sistema cerrado.")