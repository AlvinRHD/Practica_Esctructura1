#Ejercicio de practica n°1
entrada = input("Por favor ingresa un numero:")
numero = float(entrada)
minimo = int(input("Desde donde desea iniciar"))
maximo = int(input("Donde desea terminar"))
contador = 1

while contador<=10:
    producto = numero * contador
    print("{0} x {1} = {2}".format(numero,contador,producto))
    contador = contador + 1

for contador in range(minimo, maximo +1):
    producto = numero * contador
    print("{0} x {1} = {2}".format(numero,contador,producto))

#cuarto ejercicio
numero = int(input("Ingresa un numero "))
for i in range(numero, 0, -1):
    print(i)

#metodo de la burbuja para el 3
numeros = []
for i in range(0, 5):
    numero = int(input("Ingresa un numero: "))
    numeros.append(numero)

for i in range(0, len(numeros)):
    for j in range(0,len(numeros)-1):
        if numeros[j] > numeros[j+1]:
            aux = numeros[j]
            numeros[j] = numeros[j+1]
            numeros[j+1] = aux

print(numeros)