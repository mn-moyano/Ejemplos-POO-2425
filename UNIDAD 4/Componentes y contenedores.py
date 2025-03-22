#Crear una aplicación de Agenda Personal

import tkinter as tk
from idlelib import tree
from tkinter import ttk
from tkcalendar import DateEntry
import tkinter.messagebox as messagebox

def agregar_evento():
    fecha = entry_fecha.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()
    if fecha and hora and descripcion:
        tree.insert(" ", "end", values=(fecha, hora, descripcion))
        entry_fecha.set_date(" ")
        entry_hora.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")

def eliminar_evento():
    seleccionado = tree.selection()
    if seleccionado:
        if messagebox.askyesno("Confirmar", "¿Seguro que desea eliminar evento?"):
            tree.delete(seleccionado)
    else:
        messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar")

#Crear ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("500x500")

#Lista de eventos
tree_frame = tk.Frame(root)
tree_frame.pack(pady=10)

columns = ("Fecha", "Hora", "Descripcion")
tree = ttk.Treeview(tree_frame, columns=columns, show="headings")
for column in columns:
    tree.heading(column, text=column)
    tree.column(column, width=150)
tree.pack()

#Entrada de datos
entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

tk.Label(entry_frame, text="Fecha:").grid(column=0, row=0, padx=5, pady=5)
entry_fecha = DateEntry(entry_frame, width=12, background="lightblue", foreground="white")
entry_fecha.grid(column=1, row=0, padx=5, pady=5)

tk.Label(entry_frame, text="Hora:").grid(column=0, row=1, padx=5, pady=5)
entry_hora = tk.Entry(entry_frame)
entry_hora.grid(column=1, row=1, padx=5, pady=5)

tk.Label(entry_frame, text="Descripcion:").grid(column=0, row=2, padx=5, pady=5)
entry_descripcion = tk.Entry(entry_frame)
entry_descripcion.grid(column=1, row=2, padx=5, pady=5)

#Botones
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Agregar evento", command=agregar_evento).grid(column=0, row=0, padx=5, pady=5)
tk.Button(button_frame, text="Eliminar evento", command=eliminar_evento).grid(column=1, row=0, padx=5, pady=5)
tk.Button(button_frame, text="Salir", command=root.quit).grid(column=2, row=0, padx=5, pady=5)

root.mainloop()