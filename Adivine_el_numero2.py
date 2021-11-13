import random
numero = random.randint(0,100)

import entrada_menu
numero = entrada_menu.pedir_numero("Introduzca el número a adivinar ", 0, 99)
MIN = 0
MAX = 99


minimo = MIN
maximo = MAX

while True:
    intento = entrada_menu.pedir_numero("Adivine el número ", minimo, maximo)
    if intento < numero:
        print("Demasiado pequeño")
        minimo = intento + 1
    elif intento > numero:
        print("Demasiado grande")
        maximo = intento - 1
    else:
        print("Victoria")
        break





