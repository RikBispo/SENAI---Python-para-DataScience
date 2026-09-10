
	# EXERCICIO 4:Dados de quantidade de fertilizante vs produção
import tkinter as tk
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


fertilizante_kg = np.array([50, 100, 150, 200, 250]).reshape(-1, 1)
producao_ton = np.array([2.0, 3.5, 4.8, 5.5, 6.0])

#a partir daq é scikit to learn
modelo = LinearRegression()
modelo.fit(fertilizante_kg, producao_ton)

total_fertilizantes = int(input('Quantos kg de fertilizante? '))
prevista_producao = modelo.predict([[total_fertilizantes]])[0]

print(f'''Previsão de crescimento em cm: {prevista_producao}''')