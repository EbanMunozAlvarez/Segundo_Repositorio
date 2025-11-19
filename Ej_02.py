import tkinter as tk
from tkinter import Toplevel

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Ventana Principal")
ventana_principal.geometry("300x200")

# Función para abrir una ventana hija
def abrir_ventana_name():
    ventana_name = Toplevel(ventana_principal)
    ventana_name.title("Ventana Hija")
    ventana_name.geometry("250x150")
    
    etiqueta = tk.Label(ventana_name, text="Eban Muñoz Alvarez", font=("Arial", 12))
    etiqueta.pack(pady=10)
    
    boton_cerrar = tk.Button(ventana_name, text="Cerrar", command=ventana_name.destroy)
    boton_cerrar.pack(pady=10)

def abrir_ventana_msj():
    ventana_msj = Toplevel(ventana_principal)
    ventana_msj.title("Ventana Hija")
    ventana_msj.geometry("250x150")
    
    etiqueta = tk.Label(ventana_msj, text="Programa hecho en python", font=("Arial", 12))
    etiqueta.pack(pady=10)
    
    boton_cerrar = tk.Button(ventana_msj, text="Cerrar", command=ventana_msj.destroy)
    boton_cerrar.pack(pady=10)

# Botón en la ventana principal para abrir la ventana hija
boton_abrir = tk.Button(ventana_principal, text="Abrir Ventana Hija", command=abrir_ventana_name)
boton_abrir.pack(pady=20)

boton_abrir = tk.Button(ventana_principal, text="Abrir Ventana Hija", command=abrir_ventana_msj)
boton_abrir.pack(pady=20)
# Iniciar el loop principal
ventana_principal.mainloop()