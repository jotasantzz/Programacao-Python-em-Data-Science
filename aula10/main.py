


import matplotlib.pyplot as plt
import pandas as pd 
import numpy as np
# import tkinter as tk

def analise():
    dados = pd.read_csv('dados.csv')
    anos = dados['anos']
    vendas = dados['vendas']
    df = pd.DataFrame(dados)

    plt.figure(figsize = (6,6))
    plt.pie(df['vendas'], labels = df['anos'], autopct= '%1.2f%%')
    plt.show()



analise()    