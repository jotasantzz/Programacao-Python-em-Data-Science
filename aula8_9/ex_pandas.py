


import pandas as pd


dado = pd.read_csv('dados.csv')
df = pd.DataFrame(dado)

dado.to_json()
print(dado)

media = df['Idade'].mean()
mediana = df['Idade'].median()
print(df.describe())
d_user = df[df['Nome'] == 'Maria']
info_ = df.info()
agregacao = df.groupby(['Cidade', 'vendas'])['Idade'].mean

print(info_)
print('Usuario', d_user)
print('Media', media)
print('Mediana', mediana)
print(agregacao)