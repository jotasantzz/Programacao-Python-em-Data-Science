


import numpy as np

vendas = np.array([120, 90, 150, 80, 200, 110, 50, 300])

# Filtrar apenas as vendas maiores que 100
maiores_100 = vendas[vendas > 100]
print("Vendas maiores que 100:", maiores_100)

# Calcular a média
media = np.mean(vendas)
print("Média das vendas:", media)

# Contar quantas vendas ficaram abaixo da média
abaixo_media = np.sum(vendas < media)
print("Quantidade de vendas abaixo da média:", abaixo_media)

# Criar novo array dividindo cada valor pelo máximo
normalizado = vendas / np.max(vendas)
print("Valores divididos pelo máximo:", normalizado)