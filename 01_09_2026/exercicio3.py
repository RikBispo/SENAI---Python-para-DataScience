import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import tkinter as tk


dados = {
    'medias_jose': [10,5,8,9,10,5,4],
    'meses': ['fev','mar', 'abril', 'maio', 'junho', 'julho', 'agosto']
}

medias_jose = dados ['medias_jose']
meses = dados ['meses']
df = pd.DataFrame (dados)

plt.figure(figsize = (6,6))
plt.bar(df['meses'], df['medias_jose'])
plt.show()