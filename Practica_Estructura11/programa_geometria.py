import geometria

# Calcular el area y el perímetro de un círculo
radio = 5
area_circulo = geometria.calcular_area_circulo(radio)
perimetro_circulo = geometria.calcular_perimetro_circulo(radio)

# Calcular el área y el perímetro de un rectángulo
ancho = 4
alto = 6
area_rectangulo = geometria.calcular_area_rectangulo(ancho, alto)
perimetro_rectangulo = geometria.calcular_perimetro_rectangulo(ancho, alto)

# Calcular el área y el perímetro de un triángulo
base = 3
altura = 4
area_triagulo = geometria.calcular_area_triagulo(base, altura)
perimetro_triangulo = geometria.calcular_perimetro_triangulo(3, 4, 5)

print(f"Area del circulo: {area_circulo}")
print(f"Perimetro del circulo: {perimetro_circulo}")

print(f"Area del rectangulo: {area_rectangulo}")
print(f"Perimetro del rectangulo: {perimetro_rectangulo}")

print(f"Area del triangulo: {area_triagulo}")
print(f"Perimetro del triangulo: {perimetro_triangulo}")
