import numpy as np


vendas = np.array([120,90,150,80,200,110,50,300])
# iterar - percorer
l = []
for x in vendas:
    if x > 100:
        l.append(x)
print('Acima de 100', np.array(l))  


media = np.mean(vendas)
print(media)


abaixo_me = []


for v in vendas:
    if v < media:
        abaixo_me.append(v)
        maior =  max(abaixo_me)
        print('divisão', v/maior)
print('abaixo da média', np.array(abaixo_me))    


# lista_abaixo  =  np.array([x for x in vendas if vendas media])
# print(lista_abaixo)


# lista_c = np.array([x for x in vendas if x > 100])
# print(lista_c)

