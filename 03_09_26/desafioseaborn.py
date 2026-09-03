import seaborn as sns
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st


dados = pd.read_excel('dados.xlsx')
df = pd.DataFrame(dados)

media = dados['Vendas'].mean()

print ('Media de vendas geral: ', media)
mes_mais_vendas = df.groupby('Vendas')['Meses'].idxmax().sum()
mes_menos_vendas = df.groupby('Meses')['Vendas'].idxmin().sum()


print (f'''
    Mes com maior venda: {mes_mais_vendas}
    Mês com menor venda: {mes_menos_vendas}
''')    


sns.barplot(x = dados['Meses'], y = dados['Vendas'], data = dados)
plt.show()