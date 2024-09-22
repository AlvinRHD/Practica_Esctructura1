# EJERCICIOS PROPUESTOS.

# 1. Ingrese una cantidad en metros y convertir a kilómetros, sabiendo que 1km=1000m.
print("PRIMER EJERCICIO-INGRESE CANTIDAD EN M PARA CONVERTIR A KM")

m = float(input("Ingrese la cantidad que quieera en metros: "))
km = m / 1000
print(f"Equivalente en km: {km} km")


# 2. Ingrese dos números y visualizar el número mayor y número menor.
print("SEGUNDO EJERCICIO-VISUALIZAR NUMERO MAYOR Y MENOR")

numero1 = float(input("Ingrese el primer numero: "))
numero2 = float(input("Ingrese el segundo numero: "))
mayor = max(numero1, numero2)
menor = min(numero1, numero2)
print("Numero mayor", mayor)
print("Numero menor", menor)

# 3. Ingresar 5 números y visualizarlos ordenados de forma ascendente (Abstenerse del uso de la librería sort())
print("TERCER EJERCICIO-INGRESE 5 NUMEROS Y VISUALIZA DE FORMA ASCENDENTE")

numeros = []

for i in range(5):
    numero = int(input("Ingrese el número {}: ".format(i+1)))
    numeros.append(numero)

for i in range(4):
    for x in range(4 - i):
        if numeros[x] > numeros[x + 1]:
            numeros[x], numeros[x + 1] = numeros[x + 1], numeros[x]

print("Números ordenados: ")
for numero in numeros:
    print(numero)


# 4. Visualizar los n primeros números en forma descendente. (Puede utilizar While ofor)
print("CUARTO EJERCICIO-VISUALIZAR LOS NUMEROS N primeros números en forma descendente")

n = int(input("Ingrese la cantidad de numeros que desee a mostrar: "))
print("Los primeros {} números en forma descendente:".format(n))
for i in range(n, 0, -1):
    print(i)

