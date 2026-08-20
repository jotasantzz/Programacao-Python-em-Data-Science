


# Com funções crie um sistema de médias notas escolares*** 
# Com funções crie um sistema de para calcular o IMC***
# Com funções crie um jogo da adivinhação***


import random

def escolher_numero():
    return random.randint(1, 100)

def verificar_palpite(palpite, numero):
    if palpite < numero:
        return "Muito baixo!"
    elif palpite > numero:
        return "Muito alto!"
    else:
        return "Acertou!"

def jogar():
    numero = escolher_numero()
    tentativas = 0

    print("Jogo da Adivinhação!")
    print("Estou pensando em um número entre 1 e 100.")

    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        resultado = verificar_palpite(palpite, numero)
        print(resultado)

        if palpite == numero:
            print(f"Você acertou em {tentativas} tentativas!")
            break

jogar()