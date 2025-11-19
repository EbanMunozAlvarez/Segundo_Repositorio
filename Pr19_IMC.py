# CBTIS 89
# Eban Muñoz Alvarez
# 3°B Programacion MT
# calcular el imc de la persona y indicar el estado fisico

peso = float(input("escriba su peso: "))
alt = float(input("escriba su altura: "))
imc = peso/(alt*alt)

if imc < 18:
    print("tienes anorexia")
elif imc >= 18 and imc < 20:
    print("estas delgado")
elif imc >= 20 and imc < 27:
    print("peso normal")
elif imc >= 27 and imc < 30:
    print("tienes obesidad grado 1")
elif imc >= 30 and imc < 35:
    print("tienes obesidad grado 2")
elif imc >= 35 and imc < 40:
    print("tienes obesidad grado 3")
else:
    print("tienes obesidad morbida")