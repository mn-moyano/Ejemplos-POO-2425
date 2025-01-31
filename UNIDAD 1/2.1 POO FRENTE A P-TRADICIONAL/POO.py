#Crear un programa para calcular el promedio semanal de temperatura
#Crear la clase clima

class Clima:
    def __init__(self, temperatura): #Inicializar la temperatura del dia
        self.temperatura = temperatura

    def obtener_temperatura(self): #Devolver el valor de temperatura registrada
        return self.temperatura

class SemanaClima:
    def __init__(self): #Inicializar la lista de clima para cada día de la semana
        self.dias = []

    def agregar_dia(self, clima): #Agregar un objeto Clima a la lista de dias
        if len(self.dias) < 7:
            self.dias.append(clima)
        else:
            print("Solo se pueden agregar 7 dias")

    def calcular_promedio(self): #Calcula el promedio de las temperaturas de la semana
        if len(self.dias) == 7:
            total_temperaturas = sum(dia.obtener_temperatura() for dia in self.dias)
            promedio = total_temperaturas / len(self.dias)
            return promedio
        else:
            print("Faltan días para completar la semana")
            return None

#Crear una instancia de la clase Clima
semana = SemanaClima()

#Se agregan las temperaturas de cada día
semana.agregar_dia(Clima(27))
semana.agregar_dia(Clima(32))
semana.agregar_dia(Clima(30))
semana.agregar_dia(Clima(18))
semana.agregar_dia(Clima(22))
semana.agregar_dia(Clima(31))
semana.agregar_dia(Clima(21))

#Calcular el promedio semanal del clima
promedio = semana.calcular_promedio()

#Finalmente mostrar el resultado
if promedio is not None:
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")