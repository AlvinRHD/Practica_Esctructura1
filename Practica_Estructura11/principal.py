import os
from time import sleep
import calculadora as c


def menu():
    os.system("cls")
    print("\t.:: MENU ::.")
    print("[1] suma")
    print("[2] resta")
    print("[3] multiplicacion")
    print("[4] division")


while True:
    menu()
    opcion = input("Digite la opcion a realizar")

    if opcion == "1":
        num1 = int(input("Digite el primer numero: "))
        num2 = int(input("Digite el segundo numero: "))

        print(f"El resultado de la suma es: {c.suma(num1, num2)}")
        sleep(3)
        pass
    elif opcion == "2":
        num1 = int(input("Digite el primer numero: "))
        num2 = int(input("Digite el segundo numero: "))

        print(f"El resultado de la resta es: {c.resta(num1, num2)}")
        sleep(3)
        pass
    elif opcion == "3":
        num1 = int(input("Digite el primer numero: "))
        num2 = int(input("Digite el segundo numero: "))

        print(
            f"El resultado de la multiplicacion es: {c.multiplicar(num1, num2)}")
        sleep(3)
        pass
    elif opcion == "4":
        num1 = int(input("Digite el primer numero: "))
        num2 = int(input("Digite el segundo numero: "))

        print(f"El resultado de la division es: {c.division(num1, num2)}")
        sleep(3)
        pass
    else:
        print("Saliendo del programa")
        sleep(3)


# import calculadora as c

# resul_suma = c.suma(19, 3)
# resul_resta = c.resta(10, 4)
# resul_multiplicacion = c.multiplicar(6, 2)
# resul_division = c.division(8, 0)

# print("Resultado de la suma: ", resul_suma)
# print("Resultado de la resta: ", resul_resta)
# print("Resultado de la multiplicación: ", resul_multiplicacion)
# print("Resultado de la división: ", resul_division)
