import tkinter as tk
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


# EXERCICIO 1: Previsão de Notas Escolares


# Dados históricos de horas de estudo vs notas
horas_estudo = np.array([2, 4, 6, 8, 10]).reshape(-1, 1)
notas = np.array([5.0, 6.5, 7.8, 8.5, 9.2])

#a partir daq é scikit to learn
modelo = LinearRegression()
modelo.fit(horas_estudo, notas)

qntd_d_horasaserestudado = int(input('Quantas horas serão estudadas?'))
nota_prevista = modelo.predict([[qntd_d_horasaserestudado]])[0]

print(f'''Previsão: {nota_prevista:.2f}''')