


import random

# 1. Criar um array de 1 a 10
array = list(range(1, 11))

print("Array de 1 a 10:")
print(array)

# 2. Criar uma matriz 3x3 com valores aleatórios entre 0 e 1
matriz = [[random.random() for _ in range(3)] for _ in range(3)]

print("\nMatriz 3x3:")
for linha in matriz:
    print(linha)