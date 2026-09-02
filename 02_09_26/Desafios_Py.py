import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics

#Qual é a média dos números [10, 20, 30, 40, 50] usando o módulo statistics?
media = statistics.mean([10, 20, 30, 40, 50])
print(f'''A média é de: {media} ''')

#3 - Qual é a mediana dos números [3, 1, 4, 1, 5, 9, 2] usando o módulo statistics?

mediana = statistics.median([3, 1, 4, 1, 5, 9, 2])

print(f'''A mediana é {mediana}''')

#4 - Qual é a moda dos números [6, 1, 6, 7, 9, 6, 4] usando o módulo statistics?

moda = statistics.mode([6, 1, 6, 7, 9, 6, 4])

print ('A moda é: ', moda)

#5 - media com o numpy 

media = np.mean([4, 8, 15, 16, 23, 42])  
print(media)

#6 - mediana com o numpy 
mediana = np.median([7, 5, 3, 1, 9, 11, 13]) 
print(mediana)