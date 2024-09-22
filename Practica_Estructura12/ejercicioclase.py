def busqueda_binaria(lista, elemento, inicio=0, fin=None):
    if fin is None:
        fin = len(lista) - 1
    if inicio > fin:
        return - 1

    medio = (inicio + fin) // 2

    if lista[medio] == elemento:
        return medio
    elif lista[medio] < elemento:
        return busqueda_binaria(lista, elemento, medio + 1, fin)
    else:
        return busqueda_binaria(lista, elemento, inicio, medio - 1)


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
elemento = 8
indice = busqueda_binaria(lista, elemento)

if indice != -1:
    print(f"El elemento {elemento} fue encontrado en la posicion {indice}")
else:
    print(f"El elemento {elemento} no está en la lista")
