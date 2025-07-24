import random
from collections import Counter


def leer_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        numeros = archivo.read().splitlines()
        # Convertimos los números a enteros
        numeros = [int(numero) for numero in numeros]
        return numeros

def generar_numeros(numeros, cantidad):
    generados = []
    while len(generados) < cantidad:
        num = random.randint(0, 99999)
        if num not in numeros and num not in generados:  # Aseguramos que no este en 'generados' tampoco
            generados.append(num)
    return generados

def contar_numeros(numeros):
    conteo = Counter(numeros)
    repetidos = {num: conteo[num] for num in conteo if conteo[num] > 1}
    return repetidos


# Entrada de datos
cantidad_numeros = int(input("Cantidad de números a generar: "))

# Leer los números del archivo
numeros = leer_archivo('numeros-tc.txt')

# Generar una cantidad de números que no estén en el archivo
generados = generar_numeros(numeros, cantidad_numeros)

# Contar los números que se repiten
repetidos = contar_numeros(numeros)

print("=================== Probabilidad para ganar premio mayor en sorteos ===================")
print("Lista de numeros que han ganado mas de una vez: ", repetidos)
print("Lista de numeros para elegir: ", generados)