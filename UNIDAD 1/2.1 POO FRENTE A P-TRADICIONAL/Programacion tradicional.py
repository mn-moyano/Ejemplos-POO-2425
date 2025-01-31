#Crear una matriz 3D con datos diarios del clima de diferentes ciudades
#Primera dimensión: Ciudades (3 ciudades)
#Segunda dimensión: Semanas (4 semanas)
#Tercera dimensión: Días de la semana (7 días)

temperaturas = [
    [ #SantoDomingo
        [ # Semana 1
            {"day": "Lunes", "temp": 32},
            {"day": "Martes", "temp": 36},
            {"day": "Miércoles", "temp": 37},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 18},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 21}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 30},
            {"day": "Martes", "temp": 37},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 40},
            {"day": "Viernes", "temp": 42},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 23}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 36},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 33},
            {"day": "Domingo", "temp": 17}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 40},
            {"day": "Martes", "temp": 35},
            {"day": "Miércoles", "temp": 41},
            {"day": "Jueves", "temp": 33},
            {"day": "Viernes", "temp": 30},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 27}
        ]
    ],
    [  #Quito
        [  # Semana 1
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 40},
            {"day": "Jueves", "temp": 37},
            {"day": "Viernes", "temp": 41},
            {"day": "Sábado", "temp": 18},
            {"day": "Domingo", "temp": 29}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 32},
            {"day": "Miércoles", "temp": 36},
            {"day": "Jueves", "temp": 42},
            {"day": "Viernes", "temp": 43},
            {"day": "Sábado", "temp": 19},
            {"day": "Domingo", "temp": 23}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 37},
            {"day": "Miércoles", "temp": 34},
            {"day": "Jueves", "temp": 40},
            {"day": "Viernes", "temp": 42},
            {"day": "Sábado", "temp": 31},
            {"day": "Domingo", "temp": 29}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 29},
            {"day": "Martes", "temp": 40},
            {"day": "Miércoles", "temp": 45},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 35},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 26}
        ]
    ],
    [  #Manta
        [  # Semana 1
            {"day": "Lunes", "temp": 38},
            {"day": "Martes", "temp": 44},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 39},
            {"day": "Viernes", "temp": 42},
            {"day": "Sábado", "temp": 45},
            {"day": "Domingo", "temp": 26}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 46},
            {"day": "Martes", "temp": 47},
            {"day": "Miércoles", "temp": 38},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 23},
            {"day": "Domingo", "temp": 26}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 36},
            {"day": "Martes", "temp": 37},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 39},
            {"day": "Viernes", "temp": 40},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 29}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 42},
            {"day": "Martes", "temp": 33},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 29},
            {"day": "Viernes", "temp": 22},
            {"day": "Sábado", "temp": 36},
            {"day": "Domingo", "temp": 41}
        ]
    ]
]

#Calcular el promedio de temperaturas por semana
ciudades = ["Santo Domingo", "Quito", "Manta"]
for ciudad_idx, ciudad in enumerate(temperaturas) :
    for semana_idx, semana in enumerate(ciudad) :
        suma_temperaturas  = sum([dia["temp"] for dia in semana])
        promedio = round(suma_temperaturas/len(semana),2)
        print(f"El promedio de temperaturas en {ciudades[ciudad_idx]}, Semana {semana_idx + 1}: es {promedio} ")

#Calcular el promedio de temperaturas de cada ciudad
#Definir la función
def promedio_temperaturas(temperatura_ciudades) : #Primero se define la función para calcular el promedio
    promedio_temperaturas = {} #Se le da un formato de salida
    for ciudad, temperaturas in temperatura_ciudades.items() : #Se realiza el ciclo for para las temperaturas de las ciudades
        promedio = round(sum(temperaturas)/len(temperaturas),2) #Se presenta el código para el promedio de temperaturas y se redondea
        promedio_temperaturas[ciudad] = promedio #Se presenta el código que va a mostrar el promedio de temperaturas por ciudad
    return promedio_temperaturas #Este va devolver los valores escritos anteriormente las veces que sean necesarias, es decir, este código no solo sirve para las temperaturas sino que también para cualquier otro dato

#Creamos un diccionario de ciudades y temperaturas
temperatura_ciudades = {
    "Santo Domingo": [28.86,32.14,26.71,32.57],   #En este caso se les dio nombres a las ciudades y los datos de temperatura de 4 semanas
    "Quito": [31.14,30.71,34,32.71],
    "Manta": [38.14,34.43,33.43,32.43]
}

#Llamamos a la función para calcular el promedio de temperaturas
promedio_temperaturas = promedio_temperaturas(temperatura_ciudades) #Se realiza el llamamiento a la función para que presente ahora si el cálculo realizado

#Mostramos los resultados
print("Promedio de temperaturas por Ciudad: ") #Finalmente se realiza print para mostrar los resultados obtenidos de los promedios de temperaturas por ciudad
for ciudad, promedio in promedio_temperaturas.items():
    print(f"{ciudad}: {promedio}°C")