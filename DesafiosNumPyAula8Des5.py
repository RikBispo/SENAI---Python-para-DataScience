# Calcule a média dos valores do array.
# Calcule a mediana dos valores do array.
import numpy as np
numeros = np.random.randint(1,50, (5,3)) #valores de 1 a 49, numa matriz de 5x3

media = np.mean(numeros)
mediana = np.median(numeros)
print(numeros)
print (media)
print (mediana)
