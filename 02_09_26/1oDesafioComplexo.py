import statistics
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def mostrar():
    dados = pd.read_csv('dados_estudantes.csv') #lendo o arquivo 'Dados estudantes'
    df = pd.DataFrame(dados) # definindo como dataframe o aquivo lido

    # #Crie um gráfico de notas por genero
    # fix, ax = plt.subplots() #definiria o tamanho da janela, mas nao está muito bem declaro
    # ax.bar(df['gender'], df['exam_score']) #chama os eixos x (genero na tabela) e y (nota na prova)
    # plt.show()

    # #Gráfico de horas de estudos x notas
    # fix, ax = plt.subplots() 
    # ax.bar(df['study_hours_per_day'], df['exam_score'])
    # plt.show()


    #Média de notas por idade
    set_xlabel('Idade')
    set_ylabel('Nota')
    plt.plot(figsize=(10,10))
    plt.scatter(df['exam_score'], (df['age']))
    plt.grid(True)
    plt.show()
mostrar()








