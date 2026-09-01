import os


listas_temas  =  ['tema 1', 'tema 2']


for i, nomes in enumerate(listas_temas):
    os.makedirs(f"aula {nomes} - {i}", exist_ok=True)