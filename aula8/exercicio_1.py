


import numpy as np

# Criar o array
ar = np.array([1, 2, 3, 4, 5])

# Multiplicar todos os elementos por 10
m = ar * 10
print(m)

# Calcular a média
media = np.mean(ar)
print(media)

# Substituir números pares por -1
ar[ar % 2 == 0] = -1
print(ar)

# Filtrar valores maiores que 7
filtro = ar > 7
x = ar[filtro]
print(x)