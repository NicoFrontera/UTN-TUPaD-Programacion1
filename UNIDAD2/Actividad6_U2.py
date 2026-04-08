#ACTIVIDAD 6

kilovatios = int(input("Ingrese su consumo mensual de energia electria (kWh): "))

if kilovatios < 150:
    print("Consumo bajo")
elif kilovatios >= 150 and kilovatios < 300:
    print("Consumo medio")
elif kilovatios >= 300 and kilovatios < 500:
    print("Consumo alto")
else:
    print("Consumo alto")
    print("Considere medidas de ahorro energético")