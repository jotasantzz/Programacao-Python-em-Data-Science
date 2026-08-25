


import statistics


empresa1 = [2500, 2800, 3000, 9500, 12000]

empresa2 = [5000, 5200, 5300, 5400, 5500]

empresa3 = [1000, 2000, 8000, 15000, 20000]

empresa4 = [3500, 4000, 4200, 4300, 6000]

empresa5 = [1200, 1500, 1800, 2500, 10000]

def mean():
    media_empresa_1 = statistics.mean(empresa1)
    media_empresa_2 = statistics.mean(empresa2)
    media_empresa_3 = statistics.mean(empresa3)
    media_empresa_4 = statistics.mean(empresa4)
    media_empresa_5 = statistics.mean(empresa5)
    return media_empresa_1, media_empresa_2, media_empresa_3, media_empresa_4, media_empresa_5

def mode():
    moda_empresa_1 = statistics.mode(empresa1)
    moda_empresa_2 = statistics.mode(empresa2)
    moda_empresa_3 = statistics.mode(empresa3)
    moda_empresa_4 = statistics.mode(empresa4)
    moda_empresa_5 = statistics.mode(empresa5)
    return moda_empresa_1, moda_empresa_2, moda_empresa_3, moda_empresa_4, moda_empresa_5

def median():
    mediana_empresa_1 = statistics.median(empresa1)
    mediana_empresa_2 = statistics.median(empresa2)
    mediana_empresa_3 = statistics.median(empresa3)
    mediana_empresa_4 = statistics.median(empresa4)
    mediana_empresa_5 = statistics.median(empresa5)
    return mediana_empresa_1, mediana_empresa_2, mediana_empresa_3, mediana_empresa_4, mediana_empresa_5

def amplitude():
    amplitude_empresa_1 = max(empresa1) - min(empresa1)
    amplitude_empresa_2 = max(empresa2) - min(empresa2)
    amplitude_empresa_3 = max(empresa3) - min(empresa3)
    amplitude_empresa_4 = max(empresa4) - min(empresa4)
    amplitude_empresa_5 = max(empresa5) - min(empresa5)
    return amplitude_empresa_1, amplitude_empresa_2, amplitude_empresa_3, amplitude_empresa_4, amplitude_empresa_5

def variance():
    variance_empresa_1 = statistics.pvariance(empresa1)
    variance_empresa_2 = statistics.pvariance(empresa2)
    variance_empresa_3 = statistics.pvariance(empresa3)
    variance_empresa_4 = statistics.pvariance(empresa4)
    variance_empresa_5 = statistics.pvariance(empresa5)
    return variance_empresa_1, variance_empresa_2, variance_empresa_3, variance_empresa_4, variance_empresa_5

def desvio():
    desvio_empresa_1 = statistics.pstdev(empresa1)
    desvio_empresa_2 = statistics.pstdev(empresa2)
    desvio_empresa_3 = statistics.pstdev(empresa3)
    desvio_empresa_4 = statistics.pstdev(empresa4)
    desvio_empresa_5 = statistics.pstdev(empresa5)
    return desvio_empresa_1, desvio_empresa_2, desvio_empresa_3, desvio_empresa_4, desvio_empresa_5


print(f"Media: R$ {mean()}")
print(f"Moda: R$ {mode()}")
print(f"Mediana: R$ {median()}")
print(f"Amplitude: R$ {amplitude()}")
print(f"Variancia: {variance()}")
print(f"Desvio padrao: R$ {desvio()}")