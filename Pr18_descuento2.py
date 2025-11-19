# CBTIS 89
# Eban Muñoz Alvarez
# 3°B Programacion MT
# dar descuento depemdiendo del total de los articulos

art1 = int(input("escribe el nombre del primer articulo"))
art2 = int(input("escribe el nombre del segundo articulo"))
art3 = int(input("escribe el nombre del tercer articulo"))
subtotal = art1+art2+art3
des1 = subtotal*0.5
des2 = subtotal*0.10
des3 = subtotal*0.20
total = 0

if subtotal < 1000:
    total=subtotal-des1
    print("se aplico un 5 porciento de descuento, el total es de", total)
elif subtotal >=1000 and subtotal < 2500:
     total=subtotal-des2
     print("se aplico un 15 porciento de descuento, el total es de", total)
elif subtotal >= 2500:
     total=subtotal-des3
     print("se aplico un 20 porciento de descuento, el total es de", total)