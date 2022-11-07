from random import random, randint
from math import sqrt
import matplotlib.pyplot as plt
dim = 2
dim2 = 3
largo = 500
largo2 = 500
pos = [0]*dim
pos2 = [0]*dim2
lista = []
lista2 = []
replicas = 50
def paso(pos, dim):
    d = randint(0, dim-1)
    pos[d] += -1 if random() < 0.5 else 1
    return pos

def paso2(pos2, dim2):
    d1 = randint(0, dim-1)
    pos2[d1] += -1 if random() < 0.5 else 1
    return pos2

for i in range(replicas):
    posinicial = [0, 0]
    posinicial2 = [0, 0, 0]
    for t in range(largo):
        pos = paso(pos, dim)
        pos2 = paso2(pos2, dim2)
        #print(pos)
    resultado = sqrt((posinicial[0] - pos[0])**2 + (posinicial[1] - pos[1])**2)
    resultado2 = sqrt((posinicial2[0] - pos2[0])**2 + (posinicial2[1] - pos2[1])**2 + (posinicial2[2] - pos2[2])**2)  
    lista.append(resultado)
    lista2.append(resultado2)
datos = {'dimencion2': lista, 'dimencion3':lista2}
#print(lista)
#print(lista2)

fig, ax = plt.subplots()
ax.set_title('Gráfica Caja Bigote')
ax.set_xlabel('dimenciones')
ax.set_ylabel('pasos')

ax.boxplot(datos.values())
plt.xticks([1, 2], ['dimención 2', 'dimención 3'])

plt.show()
