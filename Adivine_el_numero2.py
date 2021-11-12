import random
numero = random.randint(0,100)

def pedir_numero():
    while True:
        entrada = input("Introduzca un número entre el 0 y 99: ")
        try:
            entrada = int(entrada)
        except:
            pass
        else:
            if 0 <= entrada <= 99:
                break
    return entrada

print("Introduzca un número: ")
numero = pedir_numero()

print("Intente encontrar el numero a adivinar: ")

while True:
    intento = pedir_numero()
    if intento < numero:
        print("Demasiado pequeño")
    elif intento > numero:
        print("Demasiado grande")
    else:
        print("Victoria")
        break




