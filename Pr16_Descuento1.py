# CBTIS 89
# Eban Muñoz Alvarez
# 3°B Programacion MT
# el precio de dos rticulos y si el total supera los 500$ que se haga un descuento de 10% y si no de 2%

art1 = int(input("escribe el nombre del primer articulo"))
art2 = int(input("escribe el nombre del segundo articulo"))
subtotal = art1+art2
des1 = subtotal*0.15
des2 = subtotal*0.2
total = 0

if subtotal >= 500:
    total=subtotal-des1
    print("se aplico un 15 porciento de descuento, el total es de", total)
else:
     total=subtotal-des2
     print("se aplico un 2 porciento de descuento, el total es de", total)