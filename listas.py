


# Calcular a média das notas de cada aluno.
# Identificar o aluno com a maior média.
# Calcular a média da classe (média geral de todos)


notas = [[10,10,1],[5,10,10],[5,9,8],[10,0,6]] 
nomes = ['Ana','Fernanda', 'Caio', 'Fernando']


ana  =  notas[0]
media_ana = sum(ana)/len(ana)
print('Média', nomes[0], '-', media_ana)


fernanda = notas[1]
media_fernanda = sum(fernanda)/len(fernanda)
print('Média', nomes[1], '-', media_fernanda)


caio = notas[2] 
media_caio = sum(caio)/len(caio)
print('Média', nomes[2], '-', media_caio)


fernando =  notas[3]
media_fernando = sum(fernando) / len(fernando)
print('Média', nomes[3] , '-', media_fernando)


lista_medias  =  []
lista_medias.append(media_ana)
lista_medias.append(round(media_fernanda,2))
lista_medias.append(round(media_caio,2))
lista_medias.append(round(media_fernando,2))
print('Medias: ', lista_medias)


maior_media = max(lista_medias)
posicao = lista_medias.index(maior_media)
print('O aluno com a maior média é>>>', nomes[posicao])


media_geral =  sum(lista_medias) / len(lista_medias)
print(f'Média da sala: {media_geral:.2f}')