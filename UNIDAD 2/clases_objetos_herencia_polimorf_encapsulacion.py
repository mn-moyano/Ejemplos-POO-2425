#Crear clase
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.__modelo = modelo #atributo privado

    def obtener_modelo(self): #Crear metodo
        return self.__modelo

    def descripcion(self):
        return f"Marca: {self.marca}, Modelo: {self.__modelo}"

class Moto(Vehiculo):
    def __init__(self, marca, modelo, llantas):
        super().__init__(marca, modelo)
        self.llantas = llantas

    def descripcion(self):
        return f"Marca: {self.marca}, Modelo: {self.obtener_modelo()}, Llantas: {self.llantas}"

def mostrar_descripcion(vehiculo):
    print (f" El vehículo es:",(vehiculo.descripcion()))

#Crear objetos
vehiculo = Vehiculo(marca="Toyota", modelo="BT50")
moto = Moto(marca="Suzuki", modelo="Faster", llantas=2)

#Mostrar la encapsulacion
print(f" El modelo de la moto es:",(moto.obtener_modelo()))

#Mostrar polimorfismo
mostrar_descripcion(moto)
mostrar_descripcion(vehiculo)


