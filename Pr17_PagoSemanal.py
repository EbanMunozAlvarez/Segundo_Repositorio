# CBTIS 89
# Eban Muñoz Alvarez
# 3°B Programacion MT
# dar el pago total de la semana con bono de 100 pesos
dias = int(input("escriba los dias tranajados: "))
pagdia = int(input("escribe el pago diario: "))
subtotal = pagdia*dias
total = 0

if dias >=5 and dias <= 7:
    total=subtotal+100
    print ("pago total es de: ",total," se dio un abono de 100 pesos")
elif dias <= 4:
    print ("tu salario total es: ",subtotal)
else:
    print ("no se puede llegar a una coclucion")