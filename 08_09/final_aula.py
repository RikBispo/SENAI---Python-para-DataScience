


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import filedialog


def plotar_grafico():
    
    file =  filedialog.askopenfile()
    
    d =  {
        'idades':[18,30,60,88,50,60,30],
        'salarios':[1000,5000,2000,3000,5000,5000,2500]
        }
    
    df =  pd.DataFrame(d)
    
    
    fig, grafico = plt.subplots()
    
    grafico.bar(df['idades'], df['salarios'] )
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side= tk.TOP, fill=tk.BOTH,expand=True)
        
    
    


root = tk.Tk()
root.geometry('400x400')

tk.Label(root, text = 'ANALISE DE DADOS').pack()

btn =  tk.Button(root, text = 'gere o grafico', command=plotar_grafico)
btn.pack()


root.mainloop()


