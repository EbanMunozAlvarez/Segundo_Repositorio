# CBTIS 89
# Eban Muñoz Alvarez
# 3°B Programacion MT
# calcular la utilidad de un trabajador

nombre = input ("escribe tu nombre: ")
años = int(input("escriba sus años trabajados: "))
salan = int(input("escriba su salario anual: "))
utilidad = 0
total = 0
if años < 1:
    utilidad=utilidad*0.5
    total=salan+utilidad
    print("tu salario anual es de ",total," se aplico un 5 de utilidad")
elif años >= 1 and años < 2:
    utilidad=utilidad*0.7
    total=salan+utilidad
    print("tu salario anual es de ",total," se aplico un 7 de utilidad")
elif años >= 2 and años < 5:
    utilidad=utilidad*0.10
    total=salan+utilidad
    print("tu salario anual es de ",total," se aplico un 10 de utilidad")
elif años >= 5 and años < 10:
    utilidad=utilidad*0.15
    total=salan+utilidad
    print("tu salario anual es de ",total," se aplico un 15 de utilidad")
else:
    utilidad=utilidad*0.20
    total=salan+utilidad
    print("tu salario anual es de ",total," se aplico un 20 de utilidad")