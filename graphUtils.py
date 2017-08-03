import numpy as np
import random


def randomMaxSet(adjMatrix, ite):
    #random method to determine maximal independent set
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
                vertices[:] = (v for v in vertices if independent(adjMatrix,vert,v))
                inSet.append(vert)

        if(len(inSet) > len(ret)):
            ret = inSet[:]
    return ret

def randomMaxSetEx(adjMatrix, ite, excluded):
    #same as randomMaxSet but excluding some vertices
    ret = []
    for i in range(ite):
        temp = range(len(adjMatrix))
        vertices = [x for x in temp if x not in excluded]
        random.shuffle(vertices)
        inSet = []
        while(len(vertices) > 0):
            vert = vertices.pop()
            if(full(adjMatrix,vert)):
                next
            else:
                vertices[:] = (v for v in vertices if independent(adjMatrix,vert,v))
                inSet.append(vert)

        if(len(inSet) > len(ret)):
            ret = inSet[:]
    return ret

def independent(adjMatrix, a, b):
    return not (adjMatrix[a][b] or adjMatrix[b][a])

def full(adjMatrix, a):
    #to test if vertice is alredy "complete"
    adjMatrix = np.array(adjMatrix)
    nodesBelow = (np.dot(adjMatrix[a], np.ones(len(adjMatrix), dtype=int)))
    nodesAbove = (np.dot(adjMatrix[:, a], np.ones(len(adjMatrix), dtype=int)))
    return (len(adjMatrix) + 1 - nodesBelow - nodesAbove) == 0

def listIndependent(adjMatrix, a):
    #return the list of vertices independent to a
    ret = []
    for i in range (0, a):
        if(adjMatrix[i][a] == 0):
            ret.append(i)

    for i in range(a, len(adjMatrix)):
        if(adjMatrix[a][i] == 0):
            ret.append(i)

    return ret


def main():
    #"tests"
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


