import json
#Crear la clase producto
class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad

    def to_dict(self):
        return {"id_producto": self.id_producto, "nombre": self.nombre, "cantidad": self.cantidad,"precio": self.precio}

    def __str__(self):
        return f" ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio:${self.precio}"


class Inventario:
    def __init__(self, archivo="inventario.json"):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open(self.archivo, 'r') as file:
                data = json.load(file)
                self.productos = {int(k): Producto(**v) for k, v in data.items()}
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            self.productos = {}

    def guardar_inventario(self):
        with open(self.archivo, 'w') as file:
            json.dump({k: v.to_dict() for k, v in self.productos.items()}, file, indent=4)

    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: El ID del producto ya existe")

        else:
            self.productos[producto.id_producto] = producto
            self.guardar_inventario()
            print("Producto agregado correctamente")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_inventario()
            print("Producto eliminado correctamente")
        else:
            print("Error: El ID del producto no existe")

    def actualizar_precio(self, id_producto, nuevo_precio):
        if id_producto in self.productos:
            self.productos[id_producto].actualizar_precio(nuevo_precio)
            self.guardar_inventario()
            print("Precio actualizado correctamente")
        else:
            print("Error: Producto no encontrado")

    def actualizar_cantidad(self, id_producto, nueva_cantidad):
        if id_producto in self.productos:
          self.productos[id_producto].actualizar_cantidad(nueva_cantidad)
          self.guardar_inventario()
          print("Cantidad actualizada correctamente")
        else:
          print("Error: Producto no encontrado")

    def actualizar_precio(self, id_producto, nuevo_precio):
        if id_producto in self.productos:
            self.productos[id_producto].actualizar_precio(nuevo_precio)
            self.guardar_inventario()
            print("Precio actualizado correctamente")
        else:
            print("Error: Producto no encontrado")

    def buscar_producto_nombre(self, nombre):
        resultado = [p for p in self.productos.values() if p.nombre.lower() == nombre.lower()]
        return resultado if resultado else "Producto no existe"

    def mostrar_inventario(self):
        if self.productos:
            for producto in self.productos.values():
                print(producto)
        else:
            print("El inventario está vacío.")

def menu():
    inventario = Inventario()
    while True:
        print("\n-- Sistema de Gestión de Inventario--")
        print("1. Agregar Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar precio de un producto")
        print("4. Actualizar cantidad de un producto")
        print("5. Buscar producto por nombre")
        print("6. Mostrar Inventario")
        print("7. Salir")

        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            # Agregar producto
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese el cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            inventario.agregar_producto(Producto(id_producto, nombre, cantidad, precio))

            # Aquí se debe solicitar la información del producto al usuario y llamar a inventario.agregar_producto()
        elif opcion == "2":
            # Eliminar producto
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            # Actualizar precio
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = int(input("Ingrese el cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            inventario.actualizar_precio(id_producto, precio)

        elif opcion == "4":
            # Actualizar cantidad
            id_producto = int(input("Ingrese el ID del producto a actualizar: "))
            cantidad = int(input("Ingrese la nueva cantidad: "))
            inventario.actualizar_cantidad(id_producto,cantidad)

        elif opcion == "5":
            # Buscar producto
            nombre = input("Ingrese el nombre del producto a buscar: ")
            productos = inventario.buscar_producto_nombre(nombre)
            if isinstance(productos, list):
                for producto in productos:
                    print(producto)
            else:
                print(productos)

        elif opcion == "6":
            #Mostrar inventario
            inventario.mostrar_inventario()

        elif opcion == "7":
            #Salir del sistema
            print("Saliendo...")
            break
        else:
            print("Error: ingrese un numero valido")

if __name__ == "__main__":
    menu()