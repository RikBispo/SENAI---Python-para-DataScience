# ATIVIDADE 2:
# Crie um array 2D de tamanho (5, 5) com valores aleatórios entre 0 e 100.
# Calcule a média de cada linha.
# Encontre o valor máximo e mínimo de toda a matriz.

import numpy as np
matriz = np.random.randint(0, 100, (5, 5))
print(matriz)

for  n in range(len(matriz)):
     print(np.mean(matriz[n]))

print('O menor valor da matriz é:', np.min(matriz))#valor mínimo
print('O maior valor da matriz é:', np.max(matriz))#valor máximo

