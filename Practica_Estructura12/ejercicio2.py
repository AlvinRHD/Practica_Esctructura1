import os
from time import sleep


def conteo_hacia_atras(n):
    if n <= 0:
        print("¡Despegue!")
    else:
        os.system("cls")
        print("\t.:: INICIANDO DESPEGUE ::.")
        print(n)
        sleep(2)
        conteo_hacia_atras(n - 1)


conteo_hacia_atras(10)
