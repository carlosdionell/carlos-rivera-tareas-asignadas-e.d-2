import random

matriz = [[0, 100, 0, 0, 0, 0, 0], [0, 100, 0, 0, 0, 0, 0]]
numeros = range(1, 5)
print(numeros)
# print(matriz)
for n in range(0, 2):
    for i in range(0, 2):
        for j in range(0, 2):
            numero = random.randrange(0, 3)
            matriz[i][j] = numero
            print(matriz)
