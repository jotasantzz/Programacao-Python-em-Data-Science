


import numpy as np

# Criar um array 2D (5x5) com valores aleatórios entre 0 e 100
matriz = np.random.randint(0, 101, size=(5, 5))

print("Matriz:")
print(matriz)

# Calcular a média de cada linha
media_linhas = np.mean(matriz, axis=1)

print("Média de cada linha:")
print(media_linhas)

# Encontrar o valor máximo e mínimo da matriz
maior = np.max(matriz)
menor = np.min(matriz)

print("Valor máximo:", maior)
print("Valor mínimo:", menor)