from ejemplo2Modulo import saludo
import ejemplo2Modulo as mm
from math import sqrt
import math as m

# USANDO SQRT
resultado = m.sqrt(25)
print(resultado)

# SOLO NECESITAMOS (SQRT) DE LA BIBLIOTECA DE MATH
resultado = sqrt(25)
print("Este es el resultado de la raiz: ", resultado)

# IMPORTANDO EJEMPLO2
print(mm.saludo("Alvin"))

# IMPORTANDO EJEMPLO2 DE DIFERENTE MANERA
print(saludo("Alvin"))
