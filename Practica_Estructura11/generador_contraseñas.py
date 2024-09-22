import random


def generar_contraseña(longitud):
    abecedario = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ012345678910"
    contraseña = ''.join(random.choice(abecedario) for _ in range(longitud))
    return contraseña
