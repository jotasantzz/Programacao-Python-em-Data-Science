


import numpy as np

# Array de 1 a 10
array = np.arange(1, 11)

# Adicionar 10 a todos os elementos
array = array + 10

print("Array após adicionar 10:")
print(array)

# Reshape para 2x5
array_2d = array.reshape(2, 5)

print("\nArray 2D (2x5):")
print(array_2d)