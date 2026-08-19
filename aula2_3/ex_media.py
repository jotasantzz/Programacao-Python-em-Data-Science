notas = [[10,10,10],[5,2,3],[5,9,8],[10,0,6]] 
nomes = ['Ana','Fernanda','Caio','Fernando']
ana = notas[0]
media_ana = sum(ana)/len(ana)
print("média",nomes[0],"-",media_ana)

fernanda = notas[1]
media_fernanda = sum(ana)/len(ana)
print("média",nomes[1],'-',media_fernanda)

caio = notas[2]
media_caio = sum(caio)/len(caio)
print("média",nomes[2],'-',media_caio)

fernando = notas[3]
media_fernando = sum(fernando)/len(fernando)
print("média",nomes[3],'-',media_fernando)

lista_media = []
lista_media.extend([media_ana,media_caio,media_fernanda,media_fernando])
maior_media = max(lista_media)
posição = lista_media.index(maior_media)
print("O nome da pessoa com maior média é >>>",nomes[posição])

media_geral =  sum(lista_media) / len(lista_media)
print(f'Média da sala: {media_geral:.2f}')