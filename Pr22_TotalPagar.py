# CBTIS 89
# Eban Muñoz Alvarez
# 3°B Programacion MT
# calcular mediante un ciclo cual es el  total a pagar de x cantidad de articulos

precio = float (input("escribe el precio del articulo: "))
cantidad = int (input("escribe la cantidad de productos que deseas: "))
i = 0
total = 0
for i in range (0,cantidad):
    total = total+precio
print ("el total a pagar es de: ",total)