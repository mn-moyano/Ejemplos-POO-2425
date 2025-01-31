#Crear modelaciones de situaciones del mundo real

class Carro:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.velocidad = 0

    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"El vehículo {self.marca} y modelo {self.modelo} acelero a una Velocidad: {self.velocidad}")

    def frenar(self, decremento):
        self.velocidad -= decremento
        print(f" El vehículo {self.marca} y modelo {self.modelo} freno a una velocidad: {self.velocidad}")

#Crear objetos
carro1 = Carro("Ford", "Bronco", "negro")
carro1.acelerar(60)
carro1.frenar(10)
print(f" La velocidad final del carro es: {carro1.velocidad}")