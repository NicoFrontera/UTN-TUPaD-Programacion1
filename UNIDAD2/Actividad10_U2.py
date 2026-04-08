#ACTIVIDAD 10

hemisferio = input("Ingrese en el hemisferio donde se encuentra (N/S): ")
mes = int(input("Ingrese en que mes del año se encuentra (1-12): "))
dia = int(input("Ingrese en que dia del mes se encuentra (1-31): "))

fecha = mes * 100 + dia

if hemisferio == "N" or hemisferio == "n":
    if 1221 <= fecha or fecha <= 320:
        print("Invierno")
    elif 321 <= fecha <= 620:
        print("Primavera")
    elif 621 <= fecha <= 920:
        print("Verano")
    else:
        print("Otoño")

elif hemisferio == "S" or hemisferio == "s":
    if 1221 <= fecha or fecha <= 320:
        print("Verano")
    elif 321 <= fecha <= 620:
        print("Otoño")
    elif 621 <= fecha <= 920:
        print("Invierno")
    else:
        print("Primavera")

else:
    print("Inválido")