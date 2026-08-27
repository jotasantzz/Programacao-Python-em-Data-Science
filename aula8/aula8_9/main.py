


import numpy as np



temperaturas = np.array([22, 25, 19, 30, 28, 21, 18, 33])


# Filtre apenas as temperaturas acima de 24 graus.


acima  =  np.array([n for n in temperaturas if n > 24])
print(acima)


# Calcule quantas temperaturas ficaram acima da média.


media  =  np.mean(temperaturas)
print(media)


lista_acima =  np.array([z for z in temperaturas if z > media])
print(lista_acima)



# Crie um novo array com os valores normalizados 


novo =  [t for t in temperaturas if t < media]


# (subtraia a média e divida pelo desvio padrão).


desv = round(np.std((novo)),2)
print(desv)
sub =  novo - desv
print(np.array(sub))




import numpy as np


vendas = np.array([120,90,150,80,200,110,50,300])
# iterar - percorer
l = []
for x in vendas:
    if x > 100:
        l.append(x)
print('Acima de 100', np.array(l))  


media = np.mean(vendas)
print(media)


abaixo_me = []


for v in vendas:
    if v < media:
        abaixo_me.append(v)
        maior =  max(abaixo_me)
        print('divisão', v/maior)
print('abaixo da média', np.array(abaixo_me))    


# lista_abaixo  =  np.array([x for x in vendas if vendas media])
# print(lista_abaixo)


# lista_c = np.array([x for x in vendas if x > 100])
# print(lista_c)



import numpy as np


arr = np.array (np.random.randint(0,200,(5,5)))
for x  in range(5):
    print(arr[x])
    media  =  np.mean(arr[x])
    print('media', media)  
    print('maior', max(arr[x]))
    print('menor', min(arr[x]))  




import numpy as np


arr = np.array (np.random.randint(0,100,(5,5)))


for x  in range(len(arr)):
    print(x)
    media  =  np.mean(arr[x])
    print(media)