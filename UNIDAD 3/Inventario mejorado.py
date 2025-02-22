#Gestion de inventarios
#Definicion de la clase Producto
#Esta clase modela un producto individual con ID, nombre, cantidad y precio

class Producto:
    #Constructor de la clase con cuatro parámetros: id, nombre, cantidad y precio
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = int(cantidad)
        self.precio = float(precio)

    def __str__(self):
        return f" ID: {self.id_producto}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio:${self.precio}"

#Definicion de la clase Inventario
#Esta clase maneja la colección de productos

class Inventario:
    #Constructor de la clase Inventario
    def __init__(self):
        self.productos = []
        self.cargar_inventario()

    def cargar_inventario(self):
        try:
            with open("inventario.txt",'r') as file:
                for line in file:
                    id_producto, nombre, cantidad, precio = line.strip().split(',')
                    self.productos.append(Producto(id_producto, nombre, int(cantidad), float(precio)))
        except FileNotFoundError:
            print("No se encontró el archivo de inventario, creando uno nuevo.")
            open("inventario.txt","w").close()

    def guardar_inventario(self):
      with open("inventario.txt",'w') as file:
          for producto in self.productos:
              file.write(f"{producto.id_producto},{producto.nombre},{producto.cantidad},{producto.precio}\n")

    #Metodo para agregar un nuevo producto al inventario
    def agregar_producto(self, producto):
        for p in self.productos:
            if p.id_producto == producto.id_producto:
                print("Error: producto ya registrado.")
                return
        self.productos.append(producto)
        self.guardar_inventario()
        print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                self.productos.remove(producto)
                self.guardar_inventario()
                print("Producto eliminado correctamente.")
                return
        print("Error: producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        for producto in self.productos:
            if producto.id_producto == id_producto:
                if cantidad is not None:
                   producto.cantidad = int(cantidad)
            if precio is not None:
                producto.precio = float(precio)
            self.guardar_inventario()
            print("Producto actualizado correctamente.")
            return
        print("Error: producto no encontrado.")

    def buscar_producto(self, nombre):
        resultados = [producto for producto in self.productos if nombre.lower() in producto.nombre.lower()]
        if resultados:
            print("Producto encontrado correctamente.")
            for producto in resultados:
                print(producto)
        else:
            print("Error: producto no encontrado con ese nombre.")

    def mostrar_productos(self):
        if self.productos:
            print("\n Inventario:")
            for producto in self.productos:
                print(producto)
        else:
            print("El inventario está vacío.")
#Crear la interfaz del usuario
def menu():
    inventario = Inventario()

    while True:
        print("\n1. Agregar Producto\n2. Eliminar Producto\n3. Actualizar Producto\n4. Buscar Producto\n5. Mostrar Inventario\n6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "6":
            print("Saliendo...")
            break
        elif opcion == "1":
            # Agregar producto
            id_producto = input("Ingrese el ID del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            try:
                cantidad = int(input("Ingrese el cantidad del producto: "))
                precio = input("Ingrese el precio del producto: ")
                nuevo_producto = Producto(id_producto, nombre, cantidad, precio)
                inventario.agregar_producto(nuevo_producto)
            except ValueError:
                print("Error: ingrese un numero valido")
            #Aquí se debe solicitar la información del producto al usuario y llamar a inventario.agregar_producto()
        elif opcion == "2":
            #Eliminar producto
            id_producto = input("Ingrese el ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            #Actualizar producto
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            cantidad = input("Ingrese el cantidad del producto: ")
            precio = input("Ingrese el precio del producto: ")

            cantidad = int(cantidad) if cantidad else None
            precio = int(precio) if precio else None

            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            #Buscar producto
            nombre = input("Ingrese el nombre del producto: ")
            inventario.buscar_producto(nombre)

        elif opcion == "5":
            #Mostrar inventario
            inventario.mostrar_productos()

        else:
            print("Error: ingrese un numero valido")

if __name__ == "__main__":
    menu()
