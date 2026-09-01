import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tkinter as tk


dados = {
    'anos': [2021,2022,2023,2024,2025,2026],
    'vendas': [10000,2000,30000,10000,5000,20000]
}

anos = dados ['anos']
vendas = dados ['vendas']
df = pd.DataFrame(dados)

plt.figure(figsize = (6,6))
plt.pie(df['anos'], labels = df['vendas'], autopct='%1.2f%%', colors = ["blue", "red"])
plt.show()
