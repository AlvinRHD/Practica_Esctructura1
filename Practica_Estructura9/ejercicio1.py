#Ejercicio clase
class Biblioteca:
    def __init__(self, lista_libros):
        self.libros = lista_libros

    def mostrarLibros(self):
        for libro in self.libros:
            print(f" - {libro}")

    def prestarLibros(self, libro):
        if libro in self.libros:
            print(f"Se presto el libro {libro}")
            self.libros.remove(libro)
        else:
            print(f"No encontre el libro: {libro}")

    def agregarlibro(self, libro):
        if libro not in self.libros:
            print(f"Se ha añanido el libro: {libro}")
            self.libros.append(libro)
        else:
            print("El libro ya existe")

lista_libros = ["Aprender python", "Aprender java", "Aprender js"]

biblioteca = Biblioteca(lista_libros)

while True:
    print(".:: MENU ::.")
    print("1) Mostrar Libros")
    print("2) Prestar Libros")
    print("3) Agregar Libros")
    print("4) Salir")
    opcion = int(input("Que accion desea realizar: "))

    if opcion == 1:
        print(".:: Lista de Libros ::.")
        biblioteca.mostrarLibros()
    if opcion == 2:
        libro_prestar = input("Digite el nombre del libro: ")
        biblioteca.prestarLibros(libro_prestar)
    elif opcion == 3:
        libro_agregar = input("Digite el nombre del libro: ")
        biblioteca.agregarlibro(libro_agregar)
    elif opcion == 4:
        break
    