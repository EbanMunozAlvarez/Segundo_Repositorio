# 3°B Programacion Matutino
# Autor: Eban Muñoz Alvarez
# objetivo: saludar al usuario y mostrar su edad el proximo año

nombre = input("Como te llamas? ") #pedirun dato (string)
edad = input("cuantos años tienes ")

# input siempre devuelve el texto; si necesito operar con numeros convierto:
edad = int(edad)

print() # linea en blanco
print("Encantado de conocerte, ",nombre)
print("el año que tiendras "),edad + 1, "años."