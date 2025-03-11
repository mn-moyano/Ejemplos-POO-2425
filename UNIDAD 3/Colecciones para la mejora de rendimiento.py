import json

#Crear clase libro

class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor) #Tupla inmutable
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f'{self.info[0]} por {self.info[1]} (Categoría: {self.categoria}, ISBN: {self.isbn})'

    def to_dict(self):
        return {
            "titulo": self.info[0],
            "autor": self.info[1],
            "categoria": self.categoria,
            "isbn": self.isbn
        }

#Crear la clase usuario

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = [] #Lista de libros prestados

    def __str__(self):
        return f'Usuario: {self.nombre}, ID: {self.id_usuario}, Libros Prestados: {len(self.libros_prestados)}'

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "id": self.id_usuario,
            "libros_prestados": [libro.to_dict() for libro in self.libros_prestados]
        }

#Crear la clase biblioteca

class Biblioteca:
    def __init__(self, archivo_libros='biblioteca.json', archivo_usuarios='usuarios.json'):
        self.archivo_libros = archivo_libros
        self.archivo_usuarios =archivo_usuarios
        self.libros = self.cargar_libros()
        self.usuarios = self.cargar_usuarios()

    def cargar_libros(self):
        try:
            with open(self.archivo_libros, 'r') as archivo:
                datos = json.load(archivo)
                return {isbn: Libro(**datos[isbn]) for isbn in datos}
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def cargar_usuarios(self):
        try:
            with open(self.archivo_usuarios, 'r') as archivo:
                datos= json.load(archivo)
                usuarios = {id_usuario: Usuario(datos[id_usuario]["nombre"], id_usuario) for id_usuario in datos}
                for id_usuario, usuario in usuarios.items():
                    usuario.libros_prestados =[Libro(**libro) for libro in datos[id_usuario]["libros_prestados"]]
                return usuarios
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def guardar_libros(self):
        with open(self.archivo_libros, 'w') as archivo:
            json.dump({isbn: libro.to_dict() for isbn, libro in self.libros.items()}, archivo, indent=4)

    def guardar_usuarios(self):
        with open(self.archivo_usuarios, 'w') as archivo:
            json.dump({id_usuario: usuario.to_dict() for id_usuario, usuario in self.usuarios.items()}, archivo, indent=4)

    def agregar_libro(self, libro):
        if libro.isbn not in self.libros:
            self.libros[libro.isbn] = libro
            self.guardar_libros()
            print(f'Libro agregado: {libro}')
        else:
            print(f'Libro ya existente.')

    def eliminar_libro(self, isbn):
        if isbn in self.libros:
            del self.libros[isbn]
            self.guardar_libros()
            print(f'Libro con ISBN: {isbn} eliminado')
        else:
            print(f'Libro no encontrado.')

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.usuarios:
            self.usuarios[usuario.id_usuario] = usuario
            self.guardar_usuarios()
            print(f'Usuario registrado: {usuario}')
        else:
            print(f'Usuario ya existente.')

    def eliminar_usuario(self, id_usuario):
        if id_usuario in self.usuarios:
            del self.usuarios[id_usuario]
            self.guardar_usuarios()
            print(f'Usuario eliminado: {id_usuario}')
        else:
            print(f'Usuario no encontrado.')

    def prestar_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios and isbn in self.libros:
            usuario = self.usuarios[id_usuario]
            usuario.libros_prestados.append(self.libros.pop(isbn))
            self.guardar_libros()
            self.guardar_usuarios()
            print(f'Libro prestado a {usuario.nombre}.')
        else:
            print(f'Usuario o libro no encontrado.')

    def devolver_libro(self, id_usuario, isbn):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)
                    self.libros[isbn] = libro
                    self.guardar_libros()
                    self.guardar_usuarios()
                    print(f'Libro {libro.info[0]} devuelto por {usuario.nombre}.')
                    return
            print("El usuario no tiene el libro prestado.")
        else:
            print(f'Usuario no encontrado.')

    def buscar_libro(self, criterio):
        resultado = [libro for libro in self.libros.values() if criterio.lower() in libro.info[1].lower() or criterio.lower() in libro.info[0].lower() or criterio.lower() in libro.categoria.lower()]
        if resultado:
            for libro in resultado:
                print(libro)
        else:
            print(f'Libro no encontrado.')

    def mostrar_libros(self, id_usuario):
        if id_usuario in self.usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print(f'Libros prestados a {usuario.nombre}.')
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f'Usuario no tiene libros prestados.')

def menu():
    biblioteca = Biblioteca()
    while True:
        print("\n1. Agregar Libro\n2. Eliminar Libro\n3. Registrar Usuario\n4. Eliminar Usuario\n5. Prestar Libro\n6. Devolver Libro\n7. Buscar Libro\n8. Mostrar Libros\n9. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            titulo = input("Titulo: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")
            libro = Libro(titulo, autor, categoria, isbn)
            biblioteca.agregar_libro(libro)
        elif opcion == '2':
            isbn = input("ISBN del libro a eliminar: ")
            biblioteca.eliminar_libro(isbn)
        elif opcion == '3':
            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID de usuario: ")
            biblioteca.registrar_usuario(Usuario(nombre, id_usuario))
        elif opcion == '4':
            id_usuario = input("ID de usuario a eliminar: ")
            biblioteca.eliminar_usuario(id_usuario)
        elif opcion == '5':
            id_usuario = input("ID de usuario: ")
            isbn = input("ISBN del libro a prestar: ")
            biblioteca.prestar_libro(id_usuario, isbn)
        elif opcion == '6':
            id_usuario = input("ID de usuario: ")
            isbn = input("ISBN del libro a devolver: ")
            biblioteca.devolver_libro(id_usuario, isbn)
        elif opcion == '7':
            isbn = input("Ingrese el ISBN: ")
            biblioteca.buscar_libro(isbn)
        elif opcion == '8':
          id_usuario = input("ID de usuario: ")
          biblioteca.mostrar_libros(id_usuario)
        elif opcion == '9':
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()


