# CBTIS 89 
# Eban Muñoz Alvarez
# 3°B Programacion T.M.
# programa que realiza operaciones basicas con dos numeros

numero1 = int(input("INgresar el primer numero: "))
numero2 = int(input("Ingresar el segundo numero: "))
res = 0
print("\n")
print("menu:")
print("1. sumar")
print("2. restar:")
print("3. multiplicar")
print("4. dividir")
print("5. salir")

opcion = input ("elige una opcion: ")
if opcion == "1":
    res=numero1+numero2
    print("el resultado de la SUMA es: ",res)
elif opcion == "2":
    res=numero1-numero2
    print("el resultado de la RESTA es: ", res)
elif opcion == "3":
    res=numero1*numero2
    print("el resultado de la MULTIPLICACION es: ",res)
elif opcion == "4":
    if(numero1>numero2):
        res=numero1/numero2
        print("el resultado de la DIVISION es: ",res)
    else:
        print("no puede realizar la operacion")
elif opcion == "5":
    print("saliendo del programa.")
else:
    print("opcion no valida.")