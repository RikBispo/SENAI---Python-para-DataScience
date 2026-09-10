# from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
import numpy as np


frutas_caracteristicas  =  np.array([[7,150],[8,170], [6,130], [9,180], [5,120]])
classes_frutas  =  np.array([0,0,1,0,1])


modelo = KNeighborsClassifier(n_neighbors=3)
modelo.fit(frutas_caracteristicas, classes_frutas)



nova_ = np.array([[4,120]])
classifica = modelo.predict(nova_)[0]


tipo = 'maça' if classifica == 0 else 'laranja'


print(tipo)





