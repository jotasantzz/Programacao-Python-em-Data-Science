


# 1. Criar duas matrizes 3x3

matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# 2. Calcular o produto das matrizes

produto = []

for i in range(3):
    linha = []
    for j in range(3):
        valor = 0
        for k in range(3):
            valor += matriz1[i][k] * matriz2[k][j]
        linha.append(valor)
    produto.append(linha)

print("Produto das matrizes:")
for linha in produto:
    print(linha)