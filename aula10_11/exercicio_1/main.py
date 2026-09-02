


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregar o Dataset
df = pd.read_csv("dados_estudantes.csv")


# NOTAS POR GÊNERO


media_genero = df.groupby("gender")["exam_score"].mean()

plt.figure(figsize=(8, 5))
plt.bar(media_genero.index, media_genero.values)
plt.title("Média de Notas por Gênero")
plt.xlabel("Gênero")
plt.ylabel("Média das Notas")
plt.show()



# HORAS DE ESTUDO X NOTAS


plt.figure(figsize=(8, 5))
plt.scatter(
    df["study_hours_per_day"],
    df["exam_score"]
)

plt.title("Horas de Estudo x Notas")
plt.xlabel("Horas de Estudo por Dia")
plt.ylabel("Nota")
plt.grid()
plt.show()



# MÉDIA DE NOTAS POR IDADE


media_idade = df.groupby("age")["exam_score"].mean()

plt.figure(figsize=(8, 5))
plt.plot(
    media_idade.index,
    media_idade.values,
    marker="o"
)

plt.title("Média de Notas por Idade")
plt.xlabel("Idade")
plt.ylabel("Média das Notas")

plt.xticks(np.arange(17, 25))
plt.grid()
plt.show()