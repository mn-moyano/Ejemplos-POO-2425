# Crear una interfaz
import tkinter as tk
from tkinter import messagebox

# Definir acciones
def agregar_tarea(event=None):
    tarea = entrada_tarea.get().strip()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        entrada_tarea.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No se puede agregar una tarea vacía.")

def marcar_tarea_completada(event=None):
    try:
        indice_seleccionado = lista_tareas.curselection()[0]
        tarea = lista_tareas.get(indice_seleccionado)
        if not tarea.startswith("✔ "):
            lista_tareas.delete(indice_seleccionado)
            lista_tareas.insert(indice_seleccionado, f"✔ {tarea}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para marcarla como completada.")

def eliminar_tarea(event=None):
    try:
        indice_seleccionado = lista_tareas.curselection()[0]
        lista_tareas.delete(indice_seleccionado)
    except IndexError:
        messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminarla.")

def cerrar_aplicacion(event=None):
    root.quit()

# Crear ventana principal
root = tk.Tk()
root.title("Lista de tareas")
root.geometry("500x500")

# Crear campo de entrada
entrada_tarea = tk.Entry(root, width=40)
entrada_tarea.pack(pady=10)
entrada_tarea.bind("<Return>", agregar_tarea)

# Botones
button_frame = tk.Frame(root)
button_frame.pack()

tk.Button(button_frame, text="Agregar tarea", command=agregar_tarea).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Tarea completa", command=marcar_tarea_completada).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Eliminar tarea", command=eliminar_tarea).grid(row=0, column=2, padx=5)

# Lista de tareas
lista_tareas = tk.Listbox(root, width=50, height=15)
lista_tareas.pack(pady=10)

# Atajos
root.bind("<Return>", agregar_tarea)
root.bind("c", marcar_tarea_completada)
root.bind("d", eliminar_tarea)
root.bind("<Delete>", eliminar_tarea)
root.bind("<Escape>", cerrar_aplicacion)

root.mainloop()
