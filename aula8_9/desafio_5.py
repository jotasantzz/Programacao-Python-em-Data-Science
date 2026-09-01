


import statistics

# Array de 1 a 10
array = list(range(1, 11))

# Calcular a média
media = sum(array) / len(array)

# Calcular a mediana
mediana = statistics.median(array)

print("Array:", array)
print("Média:", media)
print("Mediana:", mediana)