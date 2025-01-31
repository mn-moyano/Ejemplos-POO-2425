#Elegimos la definicion para el objetivo planeado
#Elegimos la clase y sus atributos

class Cancion:
    nombre = "Default"
    artista = "Default"
    precio = 0

    def __init__(self, nombre, artista, precio):
        self.nombre = nombre
        self.artista = artista
        self.precio = precio
    def atributos(self):
        print(self.nombre, ":", sep="")
        print("Artista:", self.artista)
        print("Precio:", self.precio)

mis_canciones = Cancion("Soltera", "Shakira", 15)
mis_canciones.atributos()
