def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


result = fibo(6)
print(result)


# # EL QUE HIZO EN CLASE
# from time import sleep


# def fibonacci_secuencia(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci_secuencia(n - 1) + fibonacci_secuencia(n - 2)


# for x in range(7):
#     print(fibonacci_secuencia(x))
#     sleep(1)
