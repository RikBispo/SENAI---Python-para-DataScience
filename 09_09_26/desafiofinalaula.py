# ATIVIDADE 3 

# CRIAR BANCO DE DADOS 3

# Você foi contratado para criar um sistema de biblioteca usando 
# SQLite + Tkinter + Matplotlib. O sistema precisa gerenciar livros e gerar relatórios.

#             id INTEGER PRIMARY KEY 
#             titulo TEXT, 
#             autor TEXT,  
#             ano INTEGER,
#             genero TEXT,
#             paginas INTEGER
            
# --------------------------------------
            
# O usuario precisa inserir os dados e em seguida, insira analise nos botões:
            
          
# O QUE OS BOTÕES DEVEM TRAZER?

# LIVROS POR ANO
# LIVROS POR GENERO
# PAGINAS POR GENERO
# ESTATISTICA GERAL
# ATUALIZAR LISTA

import tkinter as tk
from tkinter import messagebox
import sqlite3
import matplotlib.pyplot as plt

conexao = sqlite3.connect ('bancodesafiofinal.db')
cursor = conexao.cursor()

# Criar a tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER PRIMARY KEY,
        titulo TEXT, 
        autor TEXT,  
        ano INTEGER,
        genero TEXT,
        paginas INTEGER
    )
''')
conexao.commit()



def inserir_dados():
    titulo = titulo_entrada.get()
    autor = autor_entrada.get()
    cidade = cidade_entrada.get()
    ano = int(ano_entrada.get())
    genero = genero_entrada.get()
    paginas = int(paginas_entrada.get())
    cursor.execute('INSERT INTO pessoas (titulo,autor,cidade,cidade,ano,genero,paginas) VALUES(?,?,?,?,?,?,?)', (titulo,autor,cidade,ano,genero,paginas))
    conexao.commit()
#fim



# Criar a janela principal
janela = tk.Tk()
janela.title("Cadastro de Livros")

# Rótulos e campos de entrada
tk.Label(janela, text="Título:").grid(row=0, column=0, padx=10, pady=5)
titulo_entrada = tk.Entry(janela)
titulo_entrada.grid(row=0, column=1, padx=10, pady=5)

tk.Label(janela, text="Autor:").grid(row=1, column=0, padx=10, pady=5)
autor_entrada = tk.Entry(janela)
autor_entrada.grid(row=1, column=1, padx=10, pady=5)

tk.Label(janela, text="Cidade:").grid(row=2, column=0, padx=10, pady=5)
cidade_entrada = tk.Entry(janela)
cidade_entrada.grid(row=2, column=1, padx=10, pady=5)

tk.Label(janela, text="Ano:").grid(row=2, column=0, padx=10, pady=5)
ano_entrada = tk.Entry(janela)
ano_entrada.grid(row=2, column=1, padx=10, pady=5)

tk.Label(janela, text="Genero:").grid(row=2, column=0, padx=10, pady=5)
genero_entrada = tk.Entry(janela)
genero_entrada.grid(row=2, column=1, padx=10, pady=5)

tk.Label(janela, text="Qntd Páginas:").grid(row=2, column=0, padx=10, pady=5)
paginas_entrada = tk.Entry(janela)
paginas_entrada.grid(row=2, column=1, padx=10, pady=5)


# Botões
btn_inserir = tk.Button(janela, text="Inserir Dados", command=inserir_dados)
btn_inserir.grid(row=3, column=0, columnspan=2, pady=10)

btn_grafico = tk.Button(janela, text="Exibir Gráfico", command=exibir_grafico)
btn_grafico.grid(row=4, column=0, columnspan=2, pady=10)

# Iniciar o loop da aplicação
janela.mainloop()

# Fechar a conexão ao banco de dados quando a janela for fechada
conexao.close()