#Calcule a soma dos elementos do array.
#Encontre o valor máximo e mínimo do array.
import numpy as np

array = np.array([1, 2, 3, 8, 9])
maximo = np.max(array)
minimo = np.min(array)
soma = sum (array)
print ('A soma de todos os dados no array é: ', soma)
print ('O valor mínimo é: ', minimo)
print ('O valor máximo é: ', maximo)
