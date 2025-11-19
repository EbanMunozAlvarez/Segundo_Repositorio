# CBTIS 89
# Eban Muñoz Alvarez
# 3°B Programacion MT
# Calcular el promedio de 3 calificaciones y mostrar un mensaje

nombre = input ("ingrese su nombre: ")
calif1 = int (input("ingrese su primera calificacion"))
calif2 = int (input("ingrese su segunda calificacion"))
calif3 = int (input("ingrese su tercera calificacion"))
resul = (calif1+calif2+calif3)/3

if resul >= 6:
    print (nombre," tu promedio es ",resul," aprobaste")
else:
    print (nombre," tu promedio es ",resul," reprobaste")

