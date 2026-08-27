# EXERCICIO 1:
# 1 - # Lendo o arquivo CSV
# 2 - # crie um dataFrame
# 3 - # calcule a média de idade
# 4 - # mediana de idade
# 5 - # busque os dados da Maria 
# 6 - # verifique as informações tecnicas do csv
# 7 - # traga descrição básica(estatistica)
# 8 - # agregação com o groupby()

import pandas as pd
dado = pd.read_csv('dados.csv')
df = pd.DataFrame(dado)

media = df['Idade'].mean()
mediana = df['Idade'].median()
print(df.describe())
info_= df.info()
agregacao = df.groupby('Cidade')['Idade'].mean()

print(info_)
print('Usuário: ', d_user)
print ('media: ', media)
print ('Mediana ', mediana)
print(agregacao)
