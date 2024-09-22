#ejercicio1
suma =0
for i in range(1,101):
    suma += i
    print("La suma del 1 al 100 es: ", suma)


#ejercicio2
palabra = " Hola estoy programando en python"


vocales = ['a' , 'e', 'i', 'o', 'u']

for vocal in vocales:
    print(vocal , palabra.count(vocal))

#ejercicio3

numeros = [1,  4 , 6, 7  , 8,  10, 13, 2 , 9, 10, 7, 3, 8]
pares = []
impares = []

for numero in numeros:

    if numero%2 == 0:
        pares.append(numero)

    else: 
        impares.append(numero)

        print( "series:", numeros)
        print( "pares:", pares)
        print( "Impares:", impares)