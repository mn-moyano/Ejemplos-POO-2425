#Hacer un programa que se comunique entre si
#Crear la clase

class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida

    def atributos(self):
        print(self.__nombre, ":", sep="")
        print("Fuerza:", self.__fuerza)
        print("Inteligencia:", self.__inteligencia)
        print("Defensa:", self.__defensa)
        print("Vida:", self.__vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza = self.__fuerza + fuerza
        self.__inteligencia = self.__inteligencia + inteligencia
        self.__defensa = self.__defensa + defensa

    def esta_vivo(self):
        return self.__vida > 0

    def __morir(self):
        self.__vida = 0
        print(self.__nombre, "ha muerto")

    def daño(self, enemigo):
        return self.__fuerza - enemigo.__defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.__vida = enemigo.__vida - daño
        print(self.__nombre, "ha realizado", daño, "puntos de daño a", enemigo.__nombre)
        if enemigo.esta_vivo():
            print("La vida de", enemigo.__nombre, "es", enemigo.__vida)
        else:
            enemigo.__morir()
    def get_fuerza(self):
        return self.__fuerza

    def set_fuerza(self, fuerza):
        if fuerza < 0:
            print("Fuerza invalida")
        else:
            self.__fuerza = fuerza


mi_personaje = Personaje("Iori", 100, 80, 60, 5)
mi_enemigo = Personaje("Mai", 100, 50, 70, 5)

mi_personaje.set_fuerza(5)
mi_personaje.atributos()
