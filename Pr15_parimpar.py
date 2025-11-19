# CBTIS 89
# Eban Muñoz Alvarez
# 3°B Programacion MT
# lee los numeros y que indique si es par o impar

num = int(input("escriba el numero: "))
resul = num%2

if resul==1:
    print(num," el numero es impar")
else:
    print(num," el numero es par")