# CBTIS 89
# Eban Muñoz Alvarez
# 3°B Programacion MT
# Cambiar pesos a ottras monedad
import tkinter as tk
from tkinter import messagebox
from tkinter import font
from tkinter import Toplevel

def dolares():
   try:
      num = float(entrada.get())
      dolar = num /20
      resultado.config(text=f"Resultado: {dolar} dolares" )
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")
#euro
def euros():
   try:
      num = float(entrada.get())
      euro = num/22.3
      resultado.config(text=f"Resultado: {euro} euros")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")
#yenes
def yenes():
   try:
      num = float(entrada.get())
      yen = num*8.21
      resultado.config(text=f"Resultado: {yen} euros")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")
#libras
def libras():
   try:
      num1 = float(entrada.get())
      libra = num1 *0.041
      resultado.config(text=f"Resultado: {libra} libras")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")

ventana = tk.Tk()
ventana.title("Cambio de moneda")
ventana.geometry("350x230")
entrada = tk.Entry(ventana)
entrada.pack(pady=5)
boton_dolar = tk.Button(ventana, text="dolares", command=dolares)
boton_dolar.pack(pady=5)
boton_dolar = tk.Button(ventana, text="euros", command=euros)
boton_dolar.pack(pady=5)
boton_dolar = tk.Button(ventana, text="yenes", command=yenes)
boton_dolar.pack(pady=5)
boton_dolar = tk.Button(ventana, text="libras", command=libras)
boton_dolar.pack(pady=5)
resultado = tk.Label(ventana, text="Resultado:")
resultado.pack(pady=5)
ventana.mainloop()
