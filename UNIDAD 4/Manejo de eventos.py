#Crear una interfaz

import tkinter as tk
from tkinter import ttk, messagebox

def on_enter_pressed_in_entry(event=None):
    text = text_entry.get()
    if text:
        treeview.insert('', tk.END, values=(text, "Pendiente"))
        text_entry.delete(0, tk.END)
    else:
        messagebox.showwarning('Advertencia', 'Por favor, ingrese un texto antes de presionar Enter.')

def tarea_completa():
    selected_item = treeview.selection()
    if selected_item:
        text, estado = treeview.item(selected_item, 'values')
        treeview.item(selected_item, values=(text, "Completado"))
    else:
        messagebox.showwarning("Advertencia", "Por favor,selecciona una tarea para marcar.")

def eliminar_tarea():
    selected_item = treeview.selection()
    if selected_item:
        treeview.delete(selected_item)
    else:
        messagebox.showwarning("Advertencia", "Por favor,selecciona una tarea para eliminar.")

#Configurar la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("500x500")

#Campo de entrada
tk.Label(root, text="Nueva Tarea:").pack(pady=5)
text_entry = tk.Entry(root, width=40)
text_entry.pack(pady=5)
text_entry.bind("<Return>", on_enter_pressed_in_entry) #Permitir añadir con Enter

#Botones
tk.Button(root, text="Añadir Tarea", command=on_enter_pressed_in_entry).pack(pady=5)
tk.Button(root, text="Marcar como Completada", command=tarea_completa).pack(pady=5)
tk.Button(root, text="Eliminar Tarea", command=eliminar_tarea).pack(pady=5)

#Treeview para lista de tareas
treeview = ttk.Treeview(root, columns=("Tarea", "Estado"), show= "headings")
treeview.heading("Tarea", text="Tarea")
treeview.heading("Estado", text="Estado")
treeview.pack(pady=10, fill=tk.BOTH, expand=True)

root.mainloop()