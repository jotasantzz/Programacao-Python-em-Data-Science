


import matplotlib.pyplot as plt

medias_jose = [10, 5, 8, 9, 10, 5, 4]

meses = ['fev', 'mar', 'abril', 'maio', 'junho', 'julho', 'agosto']


plt.bar(meses, medias_jose, color='purple')

plt.xlabel('Meses')
plt.ylabel('Média')
plt.title('Médias do José por mês')

plt.show()