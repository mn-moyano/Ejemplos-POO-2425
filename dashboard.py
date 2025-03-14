import os

def mostrar_codigo(ruta_script):
    # Asegurarse de que la ruta al script es absoluta
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            print(f"\n--- Código de {ruta_script} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")


def mostrar_menu():
    # Definir la ruta base donde se encuentra el dashboard.py
    ruta_base = os.path.dirname(__file__)

    opciones = {
        '1': 'UNIDAD 1/1.2 TECNICAS DE PROGRAMACION/abstraccion.py',
        '2': 'UNIDAD 1/1.2 TECNICAS DE PROGRAMACION/encapsulacion.py',
        '3': 'UNIDAD 1/1.2 TECNICAS DE PROGRAMACION/herencia.py',
        '4': 'UNIDAD 1/1.2 TECNICAS DE PROGRAMACION/polimorfismo.py',
        '5': 'UNIDAD 1/2.1 POO FRENTE A P-TRADICIONAL/POO.py',
        '6': 'UNIDAD 1/2.1 POO FRENTE A P-TRADICIONAL/Programacion tradicional.py',
        '7': 'UNIDAD 1/2.2 Caracteristicas de la POO/EjemplosMundoReal_POO/Carro y Acciones.py',
        '8': 'UNIDAD 1/2.2 Caracteristicas de la POO/EjemplosMundoReal_POO/Tienda y ventas.py',
        '9': 'UNIDAD 2/clases_objetos_herencia_polimorf_encapsulacion.py',
        '10': 'UNIDAD 2/constructor y destructor.py',
        '11': 'UNIDAD 2/Identificadores y tipos de datos.py'
    } # Agregar todas las rutas de los scripts

    while True:
        print("\n********Menu Principal - Dashboard*************")
        # Imprimir las opciones del menú
        for key in opciones:
            print(f"{key} - {opciones[key]}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            # Asegurarse que el path sea absoluto
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Ejecutar el dashboard
if __name__ == "__main__":
    mostrar_menu()