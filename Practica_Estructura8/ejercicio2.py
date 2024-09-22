with open("name.txt", "w") as archivo:
    while True:
        nombre = input("Ingresa un nombre: ")
        if nombre.lower() == "s":
            break
        archivo.write(nombre + "\n")

print("Nombres guardados en 'nombres.txt'...")
