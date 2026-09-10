from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from matplotlib.backends.backend_agg import FigureCanvasAgg
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

#machine learning
from sklearn.model_selection import train_test_split #(treina e testa o machine learning)
from sklearn.metrics import accuracy_score #métrica de acurácia
from sklearn.preprocessing import LabelEncoder #nao sei!

url = 'https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv'

df = pd.read_csv(url)

#dados

df['Age'].fillna(df['Age'].median, inplace=True) #(pega a coluna idade, preenche os valores vazio, configurar a coluna)
df['Sex'] = LabelEncoder().fit_transform(df['Sex']) #transforma os sexos em 0 e 1, esse LabelEnconder serve para transformar dados só em 2 opções como 0 ou 1
df['Pclass'] = df['Pclass'].astype('category')

#interface gráfica

root = tk.Tk()#janela principal
root.title('Análise Titanics')#nome na janela
root.geometry('2000x1700') #tamanho da janela em polegadas

frame_grafico = tk.Frame() #usado para criar uma sessão dentro da janela
frame_grafico.pack(pady=20, fill=tk.BOTH, expand=True)#faz com que ele funcione e apareça

frame_controle =tk.Frame(root) 
frame_controle.pack (pady=20, fill=tk.BOTH, expand = True)

frame_resultados = tk.Frame(root)
frame_resultados.pack(pady = 10)

label_tendencia = tk.Label(frame_resultados, text='', justify=tk.LEFT)
label_tendencia.pack()

label_descricao = tk.Label(frame_resultados, text='', justify=tk.LEFT)
label_descricao.pack()

lael_previsao = tk.Label(frame_resultados, text='', justify=tk.LEFT)
label_descricao.pack()

def limpar_frame():
    for widget in frame_grafico.winfo_children():
        widget.destroy()


#botoes

btn_barras = ttk.Button(frame_controle, text= 'Grafico de Barras')
btn_barras.grid(row = 0, padx = 5, pady = 5)

btn_linhas= ttk.Button(frame_controle, text= 'Grafico de Linhas')
btn_linhas.grid(row = 1, padx = 5, pady = 5)


btn_pizza= ttk.Button(frame_controle, text= 'Grafico de Pizza')
btn_pizza.grid(row = 2, padx = 5, pady = 5)

btn_tendencia= ttk.Button(frame_controle, text= 'Grafico de Tendencia')
btn_tendencia.grid(row = 3, padx = 5, pady = 5)


btn_descricao= ttk.Button(frame_controle, text= 'Descrição')
btn_descricao.grid(row = 4, padx = 5, pady = 5)

btn_previsao= ttk.Button(frame_controle, text= 'Previsão')
btn_previsao.grid(row = 5, padx = 5, pady = 5)

#------------------------------
#funções de analise...




#----------------------------------
root.mainloop() #essa função faz a janela ficar aberta