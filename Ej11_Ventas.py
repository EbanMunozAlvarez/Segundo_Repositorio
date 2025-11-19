# CBTIS 89
# Eban Muñoz Alvarez
# 3°B Programacion MT
# Calcular el iva y total de la compra de varios articulos
import tkinter as tk
from tkinter import messagebox
from tkinter import font
from tkinter import Toplevel

def subtotal():
   try:
      num1 = float(entrada.get())
      num2 = float(entrada2.get())
      subtot = num2*num1
      resultado.config(text=f"total: {subtot}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")
def Iva():
   try:
      num1 = float(entrada.get())
      num2 = float(entrada2.get())
      subtot = num2*num1
      Iva1=subtot*0.16
      resultado.config(text=f"total: {Iva1}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")
def total():
   try:
      num1 = float(entrada.get())
      num2 = float(entrada2.get())
      subtot = num2*num1
      Iva2=subtot*0.16
      totaldef=subtot+Iva2
      resultado.config(text=f"total: {totaldef}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")

ventana = tk.Tk()
ventana.title("Ventas")
ventana.geometry("350x330")
etiqueta = tk.Label(ventana, text="Cantidad de articulos:", font=("Arial", 12))
etiqueta.pack(pady=10)
entrada = tk.Entry(ventana)
entrada.pack(pady=5)
etiqueta2 = tk.Label(ventana, text="Precio por articulo:", font=("Arial", 12))
etiqueta2.pack(pady=10)
entrada2 = tk.Entry(ventana)
entrada2.pack(pady=5)
boton_dolar = tk.Button(ventana, text="Subtotal", command=subtotal)
boton_dolar.pack(pady=5)
boton_dolar = tk.Button(ventana, text="Iva", command=Iva)
boton_dolar.pack(pady=5)
boton_dolar = tk.Button(ventana, text="Total de la compra", command=total)
boton_dolar.pack(pady=5)

resultado = tk.Label(ventana, text="Resultado:")
resultado.pack(pady=5)
ventana.mainloop()
