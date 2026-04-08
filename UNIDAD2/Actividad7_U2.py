#ACTIVIDAD 7

frase = input("Ingrese una frase o palabra: ")

if frase[-1] in ("AEIOUaeiou"):
  print(f"{frase}!")
else:
  print(frase)