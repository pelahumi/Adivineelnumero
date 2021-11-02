import random
numero = random.randint(0,99)
intento = int(input("Introduce un número: "))

def estar_en_rango (rango, intento):
    return intento in range(0,99)
print(estar_en_rango([0,100],intento))