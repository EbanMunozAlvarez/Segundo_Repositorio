# CBTIS 89
# Eban Muñoz Alvarez
# 3°B Programacion MT
# calcular que cantidad de billetes se te dara en el banco

dinero = int(input("escribe la cantidad de dinero que hay en tu cheque: 1"))
b1000 = dinero/1000
residuo = dinero%1000
dinero = residuo

b500 = dinero/500
residuo = dinero%500
dinero = residuo

b200 = dinero/200
residuo = dinero%200
dinero = residuo

b100 = dinero/100
residuo = dinero%100
dinero = residuo

b50 = dinero/50
residuo = dinero%50
dinero = residuo

b20 = dinero/20
residuo = dinero%20
dinero = residuo

m10 = dinero/10
residuo = dinero%10
dinero = residuo

m5 = dinero/5
residuo = dinero%5
dinero = residuo

m2 = dinero/2
residuo = dinero%2
dinero = residuo

m1 = dinero/1
residuo = dinero%1
dinero = residuo

print ("Billetes de 1000: ",b1000)
print ("Billetes de 500: ",b500)
print ("Billetes de 200: ",b200)
print ("Billetes de 100: ",b100)
print ("Billetes de 50: ",b50)
print ("Billetes de 20: ",b20)
print ("monedas de 10: ",m10)
print ("monedas de 5: ",m5)
print ("monedas de 2: ",m2)
print ("monedas de 1: ",m1)