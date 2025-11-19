import tkinter as tk

def sumar():
   try:
      num1 = float(entrada1.get())
      num2 = float(entrada2.get())
      suma = num1 + num2
      resultado.config(text=f"Resultado: {suma}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")
#resta
def resta():
   try:
      num1 = float(entrada1.get())
      num2 = float(entrada2.get())
      res = num1 - num2
      resultado.config(text=f"Resultado: {res}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")
#multi
def multi():
   try:
      num1 = float(entrada1.get())
      num2 = float(entrada2.get())
      mult = num1 * num2
      resultado.config(text=f"Resultado: {mult}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")
#dividir
def divi():
   try:
      num1 = float(entrada1.get())
      num2 = float(entrada2.get())
      div = num1 / num2
      resultado.config(text=f"Resultado: {div}")
   except ValueError:
      resultado.config(text="Por favor, ingresa solo números")
# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Suma de dos números")
ventana.geometry("350x230")
# Crear los cuadros de texto
entrada1 = tk.Entry(ventana)
entrada2 = tk.Entry(ventana)
# Posicionar las entradas en la ventana
entrada1.pack(pady=5)
entrada2.pack(pady=5)

# Crear botón de suma
boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack(pady=5)
#resta
boton_sumar = tk.Button(ventana, text="restar", command=resta)
boton_sumar.pack(pady=5)
#multiplicacion
boton_sumar = tk.Button(ventana, text="multiplicar", command=multi)
boton_sumar.pack(pady=5)
#division
boton_sumar = tk.Button(ventana, text="dividir", command=divi)
boton_sumar.pack(pady=5)


# Crear etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text="Resultado:")
resultado.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
