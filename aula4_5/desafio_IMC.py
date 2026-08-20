


# Com funções crie um sistema de médias notas escolares*** 
# Com funções crie um sistema de para calcular o IMC***
# Com funções crie um jogo da adivinhação***


def calcular_imc(peso, altura):
    return peso / (altura ** 2)


def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

def main():
    print("=== CALCULADORA DE IMC ===")

    peso = float(input("Digite seu peso: "))
    altura = float(input("Digite sua altura: "))

    imc = calcular_imc(peso, altura)
    classificacao = classificar_imc(imc)

    print(f"Seu IMC é: {imc:.2f}")
    print(f"Classificação: {classificacao}")


main()

