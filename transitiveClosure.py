import numpy as np
from copy import copy, deepcopy
global matrix
global neigh
global visited


def transitiveClosure(adjMatrix):
    global matrix
    global neigh
    global visited

    matrix = deepcopy(adjMatrix)
    neigh = dict()
    visited = range(len(adjMatrix))
    while(len(visited) > 0):
        num = visited[0]
        recReach(num)

    return matrix

def recReach(index):
    global matrix
    global visited
    global neigh

    reachable = []
    for i in range(index + 1, len(matrix)):
        if(matrix[index][i] == 1):
            reachable.append(i)
            if(i in neigh): 
                reachable = reachable + neigh[i]
            else:
                temp = recReach(i)
                reachable = reachable + temp
                neigh[i] = temp

    for i in reachable:
        matrix[index][i] = 1

    visited.remove(index)
    return reachable


    

def main():
    adjMatrix = [[1, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 0, 0, 1, 0, 0, 0],
                 [0, 0, 1, 1, 0, 0, 1, 0, 0],
                 [0, 0, 0, 1, 1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1]]
    m = transitiveClosure(adjMatrix)
    print(m)



