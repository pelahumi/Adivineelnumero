import random
numero = random.randint(0,100)
MIN = 0
MAX = 99

def pedir_numero(invitacion):
    invitacion += " entre " + str(MIN) + " y " + str(MAX) + ":"

    while True:
        entrada = input(invitacion)
        try:
            entrada = int(entrada)
        except:
            pass
        else:
            if MIN <= entrada <= MAX:
                break
    return entrada



numero = pedir_numero("Introduzca el número a adivinar")

print("Intente encontrar el numero a adivinar: ")

while True:
    intento = pedir_numero("Adivine el número")
    if intento < numero:
        print("Demasiado pequeño")
    elif intento > numero:
        print("Demasiado grande")
    else:
        print("Victoria")
        break




