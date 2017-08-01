import numpy as np
import time
from copy import copy, deepcopy
from sets import Set
global matrix
global neigh
global visited


def transitiveClosure(adjMatrix):
    global matrix
    global neigh
    global visited
    first = 0.0
    second = 0.0

    matrix = deepcopy(adjMatrix)
    neigh = dict()
    # visited = range(len(adjMatrix))
    # while(len(visited) > 0):
    #     num = visited[0]
    #     recReach(num)

    #ITERATIVE VERSION
    for index in range(len(matrix) - 1, -1, -1):
        reachable = Set()
        start = 0.0
        fin = 0.0

        start = time.time()
        for i in range(index + 1, len(matrix)):
            if(matrix[index][i] == 1):
                if(i not in reachable):
                    reachable.add(i)
                    reachable = reachable | neigh[i]
        fin = time.time()
        first += (fin - start)


        start = time.time()
        neigh[index] = reachable
        for i in reachable:
            matrix[index][i] = 1
        fin = time.time()
        second += (fin - start)


    print "time for reachable %0.3f" % (first * 1000.0)
    print "time for update %0.3f" % (second * 1000.0)
    return matrix

def recReach(index):
    global matrix
    global visited
    global neigh

    reachable = Set()
    for i in range(index + 1, len(matrix)):
        if(matrix[index][i] == 1):
            reachable.add(i)
            if(i in neigh): 
                reachable = reachable | neigh[i]
            else:
                temp = recReach(i)
                neigh[i] = temp
                reachable = reachable | neigh[i]

    for i in reachable:
        matrix[index][i] = 1

    visited.remove(index)
    return reachable


    

def main():
    # adjMatrix = [[1, 1, 0, 0, 0, 0, 0, 0, 0],
    #              [0, 1, 1, 0, 0, 1, 0, 0, 0],
    #              [0, 0, 1, 1, 0, 0, 1, 0, 0],
    #              [0, 0, 0, 1, 1, 0, 0, 0, 0],
    #              [0, 0, 0, 0, 1, 1, 0, 0, 0],
    #              [0, 0, 0, 0, 0, 1, 1, 0, 0],
    #              [0, 0, 0, 0, 0, 0, 1, 1, 0],
    #              [0, 0, 0, 0, 0, 0, 0, 1, 0],
    #              [0, 0, 0, 0, 0, 0, 0, 0, 1]]
    adjMatrix = np.tri(1000,1000, 500,dtype=int)
    adjMatrix = np.triu(adjMatrix)
    print(adjMatrix)
    m = transitiveClosure(adjMatrix)
    print(m)

