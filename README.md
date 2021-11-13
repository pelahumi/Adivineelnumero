# Adivineelnumero

Mi dirección de GitHub para este repositorio es: [GitHub](https://github.com/pelahumi/Adivineelnumero.git)
https://github.com/pelahumi/Adivineelnumero.git

Hemos resuelto un juego de adivinar un número del 0 al 99.

El diagrama de flujo de este ejercicio es el siguiente:

![diagrama de flujo adivine el número](/pelahumi/Adivineelnumero/Diagrama.jpg)

```import random
numero = random.randint(0,99)
intento = int(input("Introduce un número: "))
total_intentos = 0

while intento < 0 or intento > 99:
    print("Error el número tiene que estar entre 0 y 99")  
    intento = int(input("Introduce un número: "))

while intento != numero:
    if intento > numero:
        print("Demasiado grande")
        total_intentos = total_intentos + 1
        intento = int(input("Introduce un número: "))
    if intento < numero:
        print("Demasiado pequeño")
        total_intentos = total_intentos + 1
        intento = int(input("Introduce un número: "))
    if intento == numero:
        print("Enhorabuena has acertado")
        total_intentos = total_intentos + 1

print("Has utilizado: " + str(total_intentos) + " intentos")```

