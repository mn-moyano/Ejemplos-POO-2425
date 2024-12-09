#Definimos un mismo metodo para diferentes clases
#Creamos una clase

class Cafe():
    def que_soy(self):
        print("Soy un café")

class Te():
    def que_soy(self):
        print("Soy un té")

def definicion_bebida(bebida):
    bebida.que_soy()

definicion_bebida(Cafe())
definicion_bebida(Te())


