#Tipos de datos
#enteros, flotantes, string, booleanos
edad=27
peso=25.5
nombre_completo= "Madelyn Moyano"
area_de_rectangulo= 32

#CamelCase
areaRectangulo= 12
notaEstudiante= 7

#Ejemplo de uso snake_case calcular el area de un rectangulo
def area_rectangulo(base, altura):
    area = base * altura
    return area

base= 10
altura= 12
resultado= area_rectangulo(base, altura)
print(f" El resultado es: {resultado} cm2")
