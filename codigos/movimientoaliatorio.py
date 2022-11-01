from random import random, randint
dim = 5
largo = 10
pos = [0]*dim

def paso(pos, dim):
    d = randint(0, dim-1)
    pos[d] += -1 if random() < 0.5 else 1
    return pos

for t in range(largo):
    pos = paso(pos, dim)
    print(pos)
