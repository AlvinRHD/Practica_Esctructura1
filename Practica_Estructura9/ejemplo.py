class Persona:
    nombre = ""
    edad = ""
    OrientacionSexual = ""
    linaje = ""

    def __init__(self, _nombre, _edad, _orientacionSexual, _linaje):
        self.nombre = _nombre
        self.edad = _edad
        self.OrientacionSexual = _orientacionSexual
        self.linaje = _linaje

    def saltar (self):
        print("la persona está saliendo")

persona = Persona("Nadie", "20", "Hetero", "RocaFeller")

persona.saltar()
