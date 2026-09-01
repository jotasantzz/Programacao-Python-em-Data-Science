


import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo CSV
dados = pd.read_csv("vendas.csv")

# Dados
meses = dados["Mês"]
vendas = dados["Vendas"]
lucro = dados["Lucro"]


# 1. Gráfico de Pizza
plt.figure(figsize=(7, 7))

plt.pie(
    vendas,
    labels=meses,
    autopct="%1.1f%%"
)

plt.title("Distribuição de Vendas por Mês")
plt.show()


# 2. Gráfico de Dispersão
plt.figure(figsize=(7, 5))

plt.scatter(vendas, lucro, color="blue")

plt.title("Relação entre Vendas e Lucro")
plt.xlabel("Vendas")
plt.ylabel("Lucro")

plt.grid()
plt.show()


# 3. Gráfico de Barras
plt.figure(figsize=(7, 5))

plt.bar(meses, vendas, color="green")

plt.title("Vendas por Mês")
plt.xlabel("Mês")
plt.ylabel("Vendas")

plt.show()


# 4. Gráfico de Linha
plt.figure(figsize=(7, 5))

plt.plot(meses, lucro, marker="o", color="red")

plt.title("Evolução do Lucro")
plt.xlabel("Mês")
plt.ylabel("Lucro")

plt.grid()
plt.show()