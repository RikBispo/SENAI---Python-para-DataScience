import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

url = "https://gratuitos.netlify.app/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

cursos = []

for curso in soup.find_all('tr')[0]:
   # cursos.append(curso.find_all('table', class_='table').text)
    print(curso.text)