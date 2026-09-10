#
# #EXERCICIO 2: Previsão de Consumo de Energia
#

import tkinter as tk
import matplotlib as mpl
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression


# dados de temperatura x consumo de energia
temperaturas = np.array([15, 20, 25, 30, 35]).reshape(-1, 1)
consumo_kwh = np.array([120, 100, 90, 110, 150])

#a partir daq é scikit to learn
modelo = LinearRegression()
modelo.fit(temperaturas, consumo_kwh)

temp_atual = int(input('Qual a temperatura atual? Para que possamos saber o consumo'))
consumo_previsto = modelo.predict([[temp_atual]])[0]

print(f'''Previsão: {consumo_previsto:.2f}''')