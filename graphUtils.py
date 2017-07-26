import numpy as np
import random


def randomMaxSet(adjMatrix, ite):
    #
    #
    ret = []
    for i in range(ite):
        vertices = range(len(adjMatrix))
        random.shuffle(vertices)
        inSet = []
        while(len(vertices) > 0):
            vert = vertices.pop()
            if(full(adjMatrix,vert)):
                next
            else:
                #for v in vertices:
                #    if not independent(adjMatrix, vert, v):
                #        vertices.remove(v)
                vertices[:] = (v for v in vertices if independent(adjMatrix,vert,v))
                inSet.append(vert)

        if(len(inSet) > len(ret)):
            ret = inSet[:]

    
    return ret

def independent(adjMatrix, a, b):
    return not (adjMatrix[a][b] or adjMatrix[b][a])

def full(adjMatrix, a):
    adjMatrix = np.array(adjMatrix)
    nodesBelow = (np.dot(adjMatrix[a], np.ones(len(adjMatrix), dtype=int)))
    nodesAbove = (np.dot(adjMatrix[:, a], np.ones(len(adjMatrix), dtype=int)))
    return (len(adjMatrix) + 1 - nodesBelow - nodesAbove) == 0


def main():
    adjMatrix = [[1, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 0, 0, 1, 0, 0, 0],
                 [0, 0, 1, 1, 0, 0, 1, 0, 0],
                 [0, 0, 0, 1, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 1, 0, 0, 1],
                 [0, 0, 0, 0, 0, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 1],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1]]

    #print(independent(adjMatrix, 8,6))
    print(randomMaxSet(adjMatrix, 100))


