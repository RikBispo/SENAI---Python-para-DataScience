#    * é o mesmo que tudo em SQLite



import sqlite3

dados  =  sqlite3.connect('dados.db')
c = dados.cursor()

c.execute(''' CREATE TABLE IF NOT EXISTS vendas(
      
      nome TEXT NOT NULL,
      venda REAL NOT NULL
        
    
)''') 

nome  = input('nome: ')
venda = float(input('Venda: '))

c.execute('INSERT INTO vendas values(?,?)', (nome,venda))   
dados.commit()

nome  = input('nome: ')
venda = float(input('Venda: '))

c.execute('INSERT INTO vendas values(?,?)', (nome,venda))   
dados.commit()

nome  = input('nome: ')
venda = float(input('Venda: '))
    

c.execute('INSERT INTO vendas values(?,?)', (nome,venda))   
dados.commit()


c.execute('SELECT * FROM vendas')
dados =  c.fetchall()
print(dados)    
     
