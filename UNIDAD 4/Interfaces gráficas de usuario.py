import tkinter as tk
from tkinter import messagebox

def calcular_area():
    try:
        base = float(entrada_base.get())
        altura = float(entrada_altura.get())
        area = base * altura
        messagebox.showinfo("Área", f"El área del terreno es: {area} m²")
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos")

def limpiar_campos():
    entrada_base.delete(0, tk.END)
    entrada_altura.delete(0, tk.END)

#Configuración de la ventana
ventana = tk.Tk()
ventana.title("Calculadora de Área")
ventana.geometry("400x300")

#Crear etiquetas y campos de texto
etiqueta_base = tk.Label(ventana, text="Introduce la base (m) :")
etiqueta_base.pack(pady=5)
entrada_base = tk.Entry(ventana)
entrada_base.pack(pady=5)

etiqueta_altura = tk.Label(ventana, text="Introduce la altura (m) :")
etiqueta_altura.pack(pady=5)
entrada_altura = tk.Entry(ventana)
entrada_altura.pack(pady=5)

#Crear un botón para calcular el resultado
boton_calcular = tk.Button(ventana, text="Calcular área", command=calcular_area)
boton_calcular.pack(pady=5)

#Crear un botón para limpiar campos
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_campos)
boton_limpiar.pack(pady=5)

#Ejecutar la aplicación
ventana.mainloop()
