import random
numero = random.randint(0,100)
MIN = 0
MAX = 99

def pedir_numero(invitacion, minimo=MIN, maximo=MAX):
    invitacion += " entre " + str(minimo) + " y " + str(maximo) + ":"

    while True:
        entrada = input(invitacion)
        try:
            entrada = int(entrada)
        except:
            pass
        else:
            if minimo <= entrada <= maximo:
                break
    return entrada



numero = pedir_numero("Introduzca el número a adivinar", MIN, MAX)


while True:
    intento = pedir_numero("Adivine el número", minimo, maximo)
    if intento < numero:
        print("Demasiado pequeño")
        minimo = intento + 1
    elif intento > numero:
        print("Demasiado grande")
        maximo = intento - 1
    else:
        print("Victoria")
        break




