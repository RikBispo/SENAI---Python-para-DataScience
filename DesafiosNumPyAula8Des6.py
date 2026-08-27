# Adicione 10 a todos os elementos do array.
# Reshape o array 1D para um array 2D (2x5).
import numpy as np

numeros = np.random.randint(1,11, (5,1))
print (numeros)
for x in numeros:
 x + 10 
print (numeros)
reshape = np.arange(numeros).reshape((2, 5))  # 2 linhas e 5 colunas
print (reshape)