#Constructor
#Crear una clase
class Vehiculo:
    def __init__(self, marca, modelo): #Se inicializan los atributos
        self.marca = marca
        self.modelo = modelo
#Destructor
    def __del__(self): #Se procede a liberar los recursos del objeto
        print("Liberar los recursos del vehiculo")
#Crear el objeto
mi_vehiculo= Vehiculo("Ford", "F150")
print(mi_vehiculo.marca)
print(mi_vehiculo.modelo)

del mi_vehiculo

