from random import random, randint
from math import sqrt
dim = 2
largo = 5000
pos = [0]*dim

replicas = 5
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

    print(resultado)
