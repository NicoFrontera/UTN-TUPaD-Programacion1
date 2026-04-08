#EJERCICIO 5

vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_jugador = 15
danio_enemigo = 12
turno_jugador = True

nombre = input("Ingrese el nombre del gladiador: ")

while not nombre.isalpha():
    print("ERROR: El nombre tiene que tener solo letras.")
    nombre = input("Ingrese el nombre del gladiador: ")

while vida_jugador > 0 and vida_enemigo > 0:
    print("\nESTADO ACTUAL")
    print("Vida del gladiador:", vida_jugador)
    print("Vida del enemigo:", vida_enemigo)
    print("Pociones disponibles:", pociones)
    print("\n-------------------")
    print("\nMENU DE ACCIONES")
    print("1. Ataque pesado")
    print("2. Rafaga veloz")
    print("3. Curar")

    opcion = input("Elija alguna opcion (1,2 o 3): ")

    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
        print("ERROR: Opcion invalida.")
        opcion = input("\nElija alguna opcion (1,2 o 3): ")

    opcion = int(opcion)

    if opcion == 1:
        print("\nAtacas con tu espada!")
        vida_enemigo -= danio_jugador
        print(f"El enemigo recibio {danio_jugador} de daño.")
            
        if vida_enemigo > 0:
            print("El enemigo contrataca")
            vida_jugador -= danio_enemigo
            print(f"Recibiste {danio_enemigo} de daño.")

    if opcion == 2:
        print("\nTe defiendes con el escudo.")
        danio_reducido = danio_enemigo // 2
        vida_jugador -= danio_reducido
        print(f"El enemigo ataca, pero solo recibis {danio_reducido}")

    if opcion == 3:
        if pociones > 0:
            print("Te curas con la pocion.")
            pociones -= 1
            vida_jugador += 30
            if vida_jugador > 100:
                vida_jugador = 100
            print(f"Te curaste. Vida actual: {vida_jugador}")

            print("El enemigo aprovecha y ataca!")
            vida_jugador -= danio_enemigo
            print(f"Recibiste {danio_enemigo} de daño.")
        else:
            print("\nNo te quedan pociones.")

print("\n RESULTADO FINAL ")

if vida_jugador <= 0 and vida_enemigo <= 0:
    print("EMPATE! Ambos cayeron en batalla.")
elif vida_jugador > 0 and vida_enemigo <= 0:
    print(f"GANASTE! El gladiador {nombre} derroto al enemigo.")    
else:
    print("DERROTA! El enemigo te vencio.")    
