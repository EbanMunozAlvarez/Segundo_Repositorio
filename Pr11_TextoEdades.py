# CBTIS 89 
# Eban Muñoz Alvarez
# 3°B Programacion T.M.
# imprimir el nombre de la persona el texto "mayor de edad" en caso de que sea mayor o igal a 18

nombre = input("escribe tu nombre: ")
edad = int(input("escribe tu edad: "))

if edad>=18:
    print(nombre," eres mayor de edad")
else:
    print(nombre," eres menor de edad")