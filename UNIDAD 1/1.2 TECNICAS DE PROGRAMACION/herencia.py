#Herencia
#Escribimos la clase superior
class Persona:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso

    def eat(self):
        self.peso += 1
#Subclases
class Cliente(Persona):
    def __init__(self, nombre, peso, id):
        super().__init__(nombre, peso)
        self.id = id

class Operador(Persona):
    def __init__(self, nombre, peso, id):
        super().__init__(nombre, peso)
        self.id = id

Cliente1 = Cliente('Rodrigo', 160, 12)
print(Cliente1.nombre)
print(Cliente1.peso)
print(Cliente1.id)
Cliente1.eat()
print(Cliente1.peso)
print("El resultado es:", Cliente1.peso)
