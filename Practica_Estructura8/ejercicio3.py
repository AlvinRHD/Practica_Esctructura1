try:
    with open("archivo_inex.txt", "r") as archivo:
        contenido = archivo.read()
    print(contenido)
except FileNotFoundError:
    print("El archivo no existe, escribelo nuevamente, thanksss")
