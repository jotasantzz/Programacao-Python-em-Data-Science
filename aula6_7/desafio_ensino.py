


import statistics


def extrair_notas(alunos):
    """Extrai as notas de todos os alunos."""
    notas = []

    for aluno in alunos:
        notas.extend(aluno["notas"])

    return notas


def calcular_estatisticas(notas, amostral=False):
    """Calcula as estatísticas das notas."""

    if not notas:
        return None

    menor = min(notas)
    maior = max(notas)

    if amostral:
        desvio = statistics.stdev(notas)
    else:
        desvio = statistics.pstdev(notas)

    return {
        "moda": statistics.mode(notas),
        "media": statistics.mean(notas),
        "mediana": statistics.median(notas),
        "menor": menor,
        "maior": maior,
        "amplitude": maior - menor,
        "desvio_padrao": desvio
    }


def exibir_resultado(resultado):
    """Exibe as estatísticas."""

    print("\n===== ESTATÍSTICAS =====")
    print(f"Moda: {resultado['moda']:.2f}")
    print(f"Média: {resultado['media']:.2f}")
    print(f"Mediana: {resultado['mediana']:.2f}")
    print(f"Menor nota: {resultado['menor']:.2f}")
    print(f"Maior nota: {resultado['maior']:.2f}")
    print(f"Amplitude: {resultado['amplitude']:.2f}")
    print(f"Desvio padrão: {resultado['desvio_padrao']:.2f}")


def main():
    # Dados de todos os alunos
    alunos = [
        {"nome": "Ana", "notas": [8, 7, 9, 8]},
        {"nome": "Bruno", "notas": [6, 7, 5, 8]},
        {"nome": "Carlos", "notas": [9, 9, 8, 10]},
        {"nome": "Daniela", "notas": [7, 6, 7, 8]}
    ]

    # Extrair todas as notas
    notas = extrair_notas(alunos)

    # Calcular estatísticas
    resultado = calcular_estatisticas(notas)

    # Exibir resultado
    exibir_resultado(resultado)


if __name__ == "__main__":
    main()