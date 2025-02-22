#Gestion de inventarios
#Definicion de la clase Producto
#Esta clase modela un producto individual con ID, nombre, cantidad y precio

class Producto:
    #Constructor de la clase con cuatro parametros: ID, nombre, cantidad y precio
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.nombre}, Cantidad: {self.cantidad}, Precio:$ {self.precio}"

#Definicion de la clase Inventario
#Esta clase meneja la colección de productos

class Inventario:
    #Constructor de la clase Inventario
    def __init__(self):
        self.productos = {}

    #Metodo para agregar un nuevo producto al inventario
    def agregar_producto(self, producto):
        if producto.id_producto in self.productos:
            print("Error: producto ya registrado.")
        else:
            self.productos[producto.id_producto] = producto
            print("Producto registrado correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado correctamente.")
        else:
            print("Error: producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].cantidad = cantidad
            if precio is not None:
                self.productos[id_producto].precio = precio
                print("Producto actualizado correctamente.")
        else:
            print("Error: producto no encontrado.")

    def buscar_producto(self, nombre):
        for producto in self.productos.values():
            if nombre.lower() in producto.nombre.lower():
                print(producto)

    def mostrar_inventario(self):
        for producto in self.productos.values():
            print(producto)
#Crear la interfaz del usuario
def menu():
    inventario = Inventario()
    while True:
        print("\n1. Agregar Producto\n2. Eliminar Producto\n3. Actualizar Producto\n4. Buscar Producto\n5. Mostrar Inventario\n6. Salir")
        opcion = input("Seleccione una opcion: ")
        if opcion == "6":
            break
        elif opcion == "1":
            # Agregar producto
            pass #Aqui se debe solicitar la información del producto al usuario y llamar a inventario.agregar_producto()
        elif opcion == "2":
            #Eliminar producto
            pass
        elif opcion == "3":
            #Actualizar producto
            pass
        elif opcion == "4":
            #Buscar producto
            pass
        elif opcion == "5":
            #Mostrar inventario
            inventario.mostrar_inventario()

if __name__ == "__main__":
    menu()

#Creando instancias
producto1= Producto(123,"camisa_polo", 2, 52)
producto2 = Producto(153,"camiseta_algodon", 3, 85)

#Creando instancia inventario
inventario = Inventario()

#Agregando productos al inventario
inventario.agregar_producto(producto1)
inventario.agregar_producto(producto2)

#Mostrando los productos
inventario.mostrar_inventario()








