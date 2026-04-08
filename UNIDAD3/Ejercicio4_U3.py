#EJERCICIO 4

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
cant_forzar = 0
cant_hackear = 0
cant_descansar = 0

nombre_agente = input("Ingrese el nombre del agente: ")

while not nombre_agente.isalpha():
    print("\nERROR: El nombre solo debe contener letras.")
    nombre_agente = input("Ingrese el nombre del agente: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not (alarma and tiempo <= 3):
    print("\nESTADO")
    print("Energia:", energia)
    print("Tiempo:", tiempo)
    print("Cerraduras abiertas:", cerraduras_abiertas)
    print("Codigo parcial:", codigo_parcial)
    print("------------------")
    print("\nMENU PRINCIPAL")
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Seleccione alguna opcion (1,2 o 3): ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("ERROR: Opcion invalida.")
        opcion = input("Seleccione alguna opcion (1,2 o 3): ")

    opcion = int(opcion)

    if opcion == 1:
        print("\n(Forzar cerradura)")
        cant_forzar += 1
        energia -= 20
        tiempo -= 2

        if cant_forzar == 3:
            print("\nLa cerradura se trabo por forzarla 3 veces seguidas!")
            alarma = True
            cant_forzar = 0

        else:
            if energia < 40:
                print("RIESGO DE ALARMA")
                num = input("Elegi un numero del 1 al 3: ")

                while not num.isdigit() or int(num) < 1 or int(num) > 3:
                    print("ERROR: numero invalido.")
                    num = input("\nElegi un numero del 1 al 3: ")

                if int(num) == 3:
                    print("\nElegiste el numero 3, la alarma se activo!")
                    alarma = True

            if not alarma:
                cerraduras_abiertas += 1
                print(f"\nCerradura forzada con exito. Van {cerraduras_abiertas}/3")

    if opcion == 2:
        print("\n(Hackear panel)")
        cant_hackear += 1
        energia -= 10
        tiempo -= 3
        cant_forzar = 0

        print("\nIniciando hackeo")
        for x in range(1, 5):
            print(f"Paso {x} completado.")
            codigo_parcial += "A"

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            codigo_parcial = ""
            print("\nEl codigo fue suficiente y se abrio una cerradura.")
            print(f"Van {cerraduras_abiertas}/3")
        else:
            print(f"\nCodigo parcial actual: {codigo_parcial}")

    if opcion == 3:
        print("\n(Descansar)")
        cant_descansar += 1
        cant_forzar = 0

        energia += 15
        if energia > 100:
            energia = 100

        tiempo -= 1

        if alarma:
            energia -= 10
            print("La alarma esta activa, perdes 10 de energia extra.")

        print(f"\nEnergia actual: {energia}")
        print(f"Tiempo actual: {tiempo}")

if cerraduras_abiertas == 3:
    print("\nVICTORIA! Abriste la boveda.")

elif alarma and tiempo <= 3:
    print("\nDERROTA. La alarma sono y el sistema se bloqueo.")

elif energia <= 0 or tiempo <= 0:
    print("\nDERROTA. Te quedaste sin recursos.")

elif alarma:
    print("\nDERROTA. La alarma sono. Sistema bloqueado.")      

 