# CBTIS 89
# Eban Muñoz Alvarez
# 3°B Programacion MT
# calcular mediante un ciclo el promedio de 3 calificaciones y mostrar un mensaje

nombre = input("escribe tu nombre:")
i = 0
total = 0

for i in range (0,3):
    calif = int (input("escribe una calificacion:"))
    total = total+calif
resul = total/3
if resul <= 5:
    print (nombre," tu calificaion es de ",resul," reprobaste")
else
    print ()
