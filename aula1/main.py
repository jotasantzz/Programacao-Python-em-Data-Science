# 4 tipos de dados primitivos 
# TEXTO  -  STRING str
# Aluno122
# literal 

'TEXTO'
'texto'
"ISSO É UM TEXTO"
"queda d' agua" 



# dados inteiro int

1
2
10
22
36
0
-1
-2
-100


# float decimal real 

.0
5.2
3.10
5000.50
1.60
1.70
-1.5



# boleanos

True # 1
print(True +  True)
False # 0

# variaveis
# fracamente tipada
# dinamica
# estrutura de dado

n = 10
print(type(n))
# função - ação
nome = "Joao"
sobrenome = "Santos"
altura = 1.80
peso = 59.90
casada = True

n = "x"

print(type(n))
print(n)

print("sistema de imc")

altura = 1.70 # entrada
peso = 40 # entrada

imc = peso / (altura ** 2) # processamento calculo

print(imc) # saida

resultado = imc <= 18.5 and ("abaixo do normal") or imc > 18.5 and imc <= 24.9 and ("peso normal")

print(resultado)
# pemdas - parenteste exponencição multiplicação divisão adição subtração

NOME = 'Lucas'
nome = 'Julia'
Nome = 'Bruno'
nOme = 'Guilherme'

print(10 + 10)
print(10 - 10)
print(10 * 10)
print(10 / 10)
print(10 // 10)
print(10 % 10)
print(10 ** 0.5)

print(10 > 2)
print(10 < 2)
print(10 == 2)
print(10 >= 2)
print(10 <= 2)
print(10 != 2)

cidade =  input('Cidade: ')
idade  =  int(input('Idad: '))
altura = float(input('Altura: '))
peso = float(input('Peso: '))

imc = peso / altura ** 2
print(imc)

# e-commerce


print('e-commerce ')


login = input('Digite seu Login: ')
senha  =  input('Digite senha: ')


carrinho = []
total = []
produtos  =  ['computador', 'mesa', 'hd', 'tenis']
valores = [5000,250.25,500.55,540.66]


prod1 =  int(input('Escolha o ID do produto:  0,1,2,3'))
prod2 =  int(input('Escolha o ID do produto:  0,1,2,3'))
prod3 =  int(input('Escolha o ID do produto:  0,1,2,3'))


carrinho.append(produtos[prod1])
carrinho.append(produtos[prod2])
carrinho.append(produtos[prod3])


total.append(valores[prod1])
total.append(valores[prod2])
total.append(valores[prod3])


soma =  sum(total)
print('R$')
print(soma)
print('Produtos:')
print(carrinho)


