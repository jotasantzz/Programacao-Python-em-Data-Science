


import numpy as np

temperaturas = np.array([22, 25, 19, 30, 28, 21, 18, 33])

# Filtrar temperaturas acima de 24 graus
acima_24 = temperaturas[temperaturas > 24]
print("Temperaturas acima de 24:", acima_24)

# Calcular a média
media = np.mean(temperaturas)
print("Média:", media)

# Contar quantas temperaturas ficaram acima da média
quantidade = np.sum(temperaturas > media)
print("Quantidade acima da média:", quantidade)

# Normalizar os valores
normalizados = (temperaturas - media) / np.std(temperaturas)
print("Valores normalizados:", normalizados)