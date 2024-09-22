import math


def calcular_area_circulo(radio):
    return math.pi * radio**2


def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio


def calcular_area_rectangulo(ancho, alto):
    return ancho * alto


def calcular_perimetro_rectangulo(ancho, alto):
    return 2 * (ancho + alto)


def calcular_area_triagulo(base, altura):
    return 0.5 * base * altura


def calcular_perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3
