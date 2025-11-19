import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo de Widgets en Tkinter")
ventana.geometry("300x300")

# Etiqueta de texto
etiqueta = tk.Label(ventana, text="Nombre:", font=("Arial", 12))
etiqueta.pack(pady=10)

# Cuadro de texto
nombre = tk.Entry(ventana, font=("Arial", 12))
nombre.pack(pady=5)

# Etiqueta de texto
etiqueta2 = tk.Label(ventana, text="Apellido:", font=("Arial", 12))
etiqueta2.pack(pady=10)

# Cuadro de texto
apellido = tk.Entry(ventana, font=("Arial", 12))
apellido.pack(pady=5)

# Botón que responde a un evento
def mostrar_texto():
    texto2=apellido.get()
    texto = nombre.get()
    etiqueta_resultado.config(text=f"Escribiste: {texto} {texto2}")

boton = tk.Button(ventana, text="Mostrar texto", command=mostrar_texto)
boton.pack(pady=10)

# Etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="", font=("Arial", 12), fg="blue")
etiqueta_resultado.pack(pady=5)

# Iniciar el loop principal
ventana.mainloop()
