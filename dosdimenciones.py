from random import random, randint
from math import sqrt
import matplotlib.pyplot as plt
dim = 2
largo = 50
pos = [0]*dim
lista = []
replicas = 50
def paso(pos, dim):
    d = randint(0, dim-1)
    pos[d] += -1 if random() < 0.5 else 1
    return pos
for i in range(replicas):
    posinicial = [0, 0]
    for t in range(largo):
        pos = paso(pos, dim)
        #print(pos)
    resultado = sqrt((posinicial[0] - pos[0])**2 + (posinicial[1] - pos[1])**2) 
    lista.append(resultado)
print(lista)
plt.boxplot(lista)
plt.show()
