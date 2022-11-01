import matplotlib.pyplot as plt
from random import randint
import statistics
import math
largo = 1000
altura = largo
radio = largo
npuntos = 0
ndentro = 0
radio2 = radio*radio

replicas = 10
numerosaliatorios = 10000


promediopi = []
listareplicas = []
listapromedios = []
for j in range(replicas):
    for i in range(1,numerosaliatorios):
        x = randint(0,largo)
        y = randint(0,largo)
        npuntos += 1
        if x*x + y*y <= radio2:
            ndentro += 1
        pi = ndentro * 4 /npuntos
        promediopi.append(pi)
    listareplicas.append(j)
    listapromedios.append(statistics.mean(promediopi))
plt.plot(listareplicas,listapromedios)
plt.plot(listareplicas, [math.pi for z in range(replicas)])
plt.xlabel('Replicas')
plt.ylabel('Valores de pi')
plt.title('Convergencia de pi')
plt.show()
