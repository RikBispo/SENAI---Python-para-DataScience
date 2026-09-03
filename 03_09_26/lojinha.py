import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt


url = 'https://bea3853.github.io/site-ecommerce/'
# headers = {'User-Agent': 'Mozilla/5.0'}
reponse = requests.get(url)


soup = BeautifulSoup(reponse.text, 'html.parser')


nome = []
precos = []
avaliacoes = []


# -----------------


for produto in soup.find_all('div', class_ = 'produto'):
    nome.append(produto.find('h2').text)
    precos.append(float(produto.find('span'), class_='preco').text.replace('R$','').replace('.',',').replace(',','.'))
    avaliacoes.append(float(produto.find('span', class_='avaliacoes').text))





print(soup)