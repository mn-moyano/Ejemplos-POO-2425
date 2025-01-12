#Crear modelaciones de situaciones del mundo real
class Producto:
    def __init__(self, nombre, precio, descripcion):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}: {self.descripcion}"

class Cliente:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.carrito = Carrito()

    def agregar_producto_al_carrito(self, producto, cantidad):
        self.carrito.agregar_producto(producto, cantidad)
    def ver_carrito(self):
        return self.carrito.mostrar_carrito()

class Carrito:
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto, cantidad):
        if producto.nombre in self.productos:
            self.productos[producto.nombre]['cantidad'] += cantidad
        else:
            self.productos[producto.nombre] = {'producto': producto, 'cantidad': cantidad}

    def mostrar_carrito(self):
        if not self.productos:
            return "Tu carrito está vacío"
        carrito_str = ""
        for item in self.productos.values():
            carrito_str += f"{item['producto'].nombre} - Cantidad: {item['cantidad']} -Precio: ${item["producto"].precio:.2f} cada uno\n"
        return carrito_str

    def calcular_total(self):
        total = 0
        for item in self.productos.values():
            total += item['producto'].precio * item['cantidad']
        return total

#Crear pedido
class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = self.copiar_productos(cliente.carrito.productos)
        self.total = cliente.carrito.calcular_total()

    def copiar_productos(self, productos):
        return {nombre: {'producto': item['producto'], 'cantidad': item['cantidad']} for nombre, item in productos.items()}

    def confirmar_pedido(self):
        return f"Pedido confirmado para {self.cliente.nombre}. Total: ${self.total:.2f}"

#Crear pago
class Pago:
    def __init__(self, pedido, metodo_pago):
        self.pedido = pedido
        self.metodo_pago =metodo_pago
        self.estado ="Pendiente"

    def realizar_pago(self ):
        self.estado = "Realizado"
        return f"Pago realizado con éxito. Metódo de pago: {self.metodo_pago}. Total: ${self.pedido.total:.2f}"
#Crear envio
class Envio:
    def __init__(self, pedido, direccion_envio):
        self.pedido = pedido
        self.direccion_envio = direccion_envio
        self.estado ="Pendiente"

    def procesar_envio(self):
        self.estado = "Enviado"
        return f"El pedido ha sido enviado a {self.direccion_envio}. Estado de envío: {self.estado}"

#Crear algunos productos
producto1 = Producto("Camiseta", 25, "Camiseta de algodon, talla M, color blanco")
producto2 = Producto("Pantalón", 50, "Pantalón jean, talla 12, color azul")

#Crear un cliente
cliente = Cliente("Nina", "Moyano")


#Agregar productos al carrito
cliente.agregar_producto_al_carrito(producto1, 2)
cliente.agregar_producto_al_carrito(producto2, 2)

#Ver el carrito
print("Carrito de compras de", cliente.nombre)
print(cliente.ver_carrito())

#Crear un pedido
pedido= Pedido(cliente)

#Confirmar pedido
print("\n", pedido.confirmar_pedido())

#Realizar el pago
pago = Pago(pedido, "Tarjeta de crédito")
print(pago.realizar_pago())

#Procesar el envío
envio= Envio(pedido, "Av. Río Yamboya y Varsovia")
print(envio.procesar_envio())