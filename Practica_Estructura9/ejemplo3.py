#Polimorfismo
class Perro:
    def sonido(self):
        print("uauuuuuuuu!!G!!!")
    pass

class Gato:
    def sonido(self):
        print("Miauuuu!!!!!!!")
    pass

class Vaca:
    def sonido(self):
        print("Muuuuuuuuuu!!!!")
    pass

perro = Perro()
gato = Gato()
vaca = Vaca()

animales = [perro, gato, vaca, gato, perro, vaca]

for animal in animales:
    animal.sonido()