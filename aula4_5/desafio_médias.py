


# Com funções crie um sistema de médias notas escolares*** 
# Com funções crie um sistema de para calcular o IMC***
# Com funções crie um jogo da adivinhação***


escola = input("Digite o nome da escola: ")

def soma():
    global nome
    nome = input("Digite o nome do aluno: ")

    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))

    return (n1 + n2 + n3) / 3

def situacao():
    media = soma()
    if media >= 7:
        return "Aprovado"
    elif media <= 5:
        return "Reprovado"

    print("---RESULTADO---")
    print(f"Escola{escola}")
    soma()
    print(f"Aluno{nome}")
    print("Média", round(soma(), 2))
    print(f"Situação{media}")

print(situacao())









