
#EXERCICIO 3: Previsão de Crescimento de Plantas

import tkinter as tk
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


# Dados de dias desde plantio vs altura da planta
dias = np.array([10, 20, 30, 40, 50]).reshape(-1, 1)
altura_cm = np.array([5, 12, 18, 25, 30])

#a partir daq é scikit to learn
modelo = LinearRegression()
modelo.fit(dias, altura_cm)

qntd_dias = int(input('Quantas dias essa planta tem de vida?'))
crescimento_previsto = modelo.predict([[qntd_dias]])[0]

print(f'''Previsão de crescimento em cm: {crescimento_previsto}''')