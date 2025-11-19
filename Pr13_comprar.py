# CBTIS 89 
# Eban Muñoz Alvarez
# 3°B Programacion T.M.
# si los numeros son iguales es multiplica, mayor suma y menor resta

num1 = int(input("escribe el primer numero: "))
num2 = int(input("escribe el segundo numero: "))
resul = 0

if num1 == num2:
    resul=num1*num2
    resul=num1*num2
    print("el resultado de la MULTIPLICACION es: ",resul)
elif num1 >= num2:
    resul=num1+num2
    print("el resultado de la SUMA es: ",resul)
else:
    resul=num1-num2
    print("el resultado de la RESTA es: ",resul)
