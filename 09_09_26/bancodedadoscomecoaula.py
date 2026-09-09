import sqlite3 #importado p usar o sqlite
import pandas as pd

banco = sqlite3.connect('dados.db')#cria o arquivo de banco de dados

#obs: instalar a extensão SQLite DB Viewer é mt boa e gratuita


cursor = banco.cursor()#isso aqui serve para digitar sql no arquivo python, essencial
#agora é possível digitar sql diretamente do python

#o comando abaixo cria uma tabela se ela n existir com o mesmo nome
cursor.execute(''' CREATE TABLE IF NOT EXISTS clientes(
               
               id INTEGER PRIMARY KEY,
               nome TEXT NOT NULL,
               email TEXT NOT NULL,
               salario TEXT REAL NOT NULL,
               cargo TEXT NOT NULL
               
               
               )''') #oq vier dps de clientes e estiver em () cria uma coluna na tabela
#depois disso você define o tipo de dado que vai receber e se pode ou não estar não recebendo um dado

#CREATE cria a tabela
#INSERT insere dados na tabela
cursor.execute('INSERT INTO clientes values(?,?,?,?,?)', (10,'Ana','ana@gmail.com',4500.0,'Analista')) #serve para adicionar os dados no bd
#essas interrogações são responsável por falar quais colunas estão sendo preenchidas
# depois das interrogações na parte do '(1,'Ana','ana@gmail.com',4500.0,'Analista')' segue a ordem da tabela, exemplo, o 1 se reere ao ID, 'Ana refere a Ana
# assim como na ordem de declaração onde 'id' é seguido de 'nome'

banco.commit() # esse comando salva o dado no banco de dados 

cursor.execute('INSERT INTO clientes values(?,?,?,?,?)', (11,'Kaio','ana@gmail.com',3500.0,'Estagiário')) #serve para adicionar os dados no bd
banco.commit()

cursor.execute('INSERT INTO clientes values(?,?,?,?,?)', (12,'Felipe','ana@gmail.com',1500.0,'Menor Aprendiz')) #serve para adicionar os dados no bd
banco.commit()

cursor.execute('INSERT INTO clientes values(?,?,?,?,?)', (13,'Bernardo','ana@gmail.com',9500.0,'Coordenador')) #serve para adicionar os dados no bd
banco.commit()

cursor.execute('SELECT * FROM clientes') # esse * significa all
DADOS_ = cursor.fetchall() #transforma tudo oq tem na tabela, e voce transforma tudo numa lista com tuplas dentro

print(DADOS_)

#SELCIONAR COLUNAS:
cursor.execute('SELECT nome, salario FROM clientes')
df = pd.DataFrame(DADOS_)
df.to_csv('clientes.csv', index=False)
dados_ = cursor.fetchall()
