


import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


url = 'https://jotasantzz.github.io/Site-Ecommerce/'
# headers = {'User-Agent': 'Mozilla/5.0'}
reponse = requests.get(url)


soup = BeautifulSoup(reponse.text, 'html.parser')


nome = []
precos = []
avaliacoes = []


# -----------------


for produto in soup.find_all('div', class_ = 'produto'):
    nome.append(produto.find('h2').text)
    precos.append(float(produto.find('span', class_='preco').text.replace('R$','').replace('.','').replace(',','.').strip()))
    avaliacoes.append(float(produto.find('span', class_='avaliacoes').text))
print(nome)
print(avaliacoes)
print(precos)