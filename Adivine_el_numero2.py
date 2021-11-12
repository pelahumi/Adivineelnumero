import random
numero = random.randint(0,100)

print("Introduzca un número: ")

while True:
    numero = input("Introduzca un número entre el 0 y 99 incluídos")

    try:
        numero = int(numero)
    except:
        pass
    else: 
        if 0 <= numero <= 99:
            break

print("Intente encontrar el numero a adivinar: ")

while True:
    while True:
        intento = input("Introduzca un número entre el 0 y 99 incluídos: ")

        try:
            numero = int(numero)
        except:
            pass
        else:
            if 0 <= numero <=99:
                break

                
    if intento < numero:
        print("Demasiado pequeño")
    elif intento > numero:
        print("Demasiado grande")
    else:
        print("Victoria")
        break




