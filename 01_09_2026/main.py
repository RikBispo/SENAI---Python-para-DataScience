import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tkinter as tk

def analise ():
    dados = pd.read_csv('dados.csv')
    anos = dados['ano']
    vendas = dados['vendas']
    df = pd.DataFrame(dados)
    cores = ['red', 'yellow', 'green', 'pink']

    #grafico de pizza
    plt.figure(figsize = (6,6))
    plt.pie(df['vendas'], labels = df['ano'], autopct='%1.2f%%', colors = cores)
    plt.show()

    #grafico de barras

    plt.figure(figsize=(6,6))
    plt.bar(df['ano'], df['vendas'])
    plt.show()

    #grafico de linha
    plt.figure(figsize=(7,10))
    plt.plot(df['ano'], df['vendas'], marker = 'o', linestyle = '-', color = 'red')
    plt.grid(True)
    plt.show()

    #grafico de correlação (ou scatter, funciona 2 variáveis)
    plt.plot(figsize=(7,10))
    plt.scatter(df['vendas'], df['lucro'], color = 'orange')
    plt.grid(True)
    plt.show()
analise()