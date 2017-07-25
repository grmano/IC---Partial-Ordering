import numpy as np
import random
import argparse
import math
import heapq

global adjMatrix
global missingEdges

def isNeigh(a, b):
    #since is a directed graph, to test if two vertices are neighbours
    #they to have "sorted"
    global adjMatrix
    if(a < b):
        return adjMatrix[a][b]
    else:
        return adjMatrix[b][a]

def choiceHandler(vertices):
    #Updates adjMatrix with the direct edges from comparison
    global adjMatrix
    size = len(vertices)
    vertices.sort()

    for i in vertices:
        for j in vertices[vertices.index(i):]:
            adjMatrix[i][j] = True

def computeTransitive():
    global adjMatrix
    #compute the transitive matrix using matrix multiplication
    #Naive way

    #TODO: use fast exponentiation

    dimension = len(adjMatrix)
    numberOfTimes = int(math.ceil(math.sqrt(dimension)))

    for i in range(numberOfTimes):
        adjMatrix = np.matmul(adjMatrix,adjMatrix)

def updateMissingEdges():
    global adjMatrix
    global missingEdges
    #this function iterates through the rows of the matrix
    #checking if the vertice is already complete(ordered), and updating
    #the list that keeps track of how many missing edges each vertices has
    count = 0
    for row in adjMatrix:
        nodesBelow = (np.dot(adjMatrix[count], np.ones(len(adjMatrix), dtype=int)))
        nodesAbove = (np.dot(adjMatrix[:, count], np.ones((len(adjMatrix)), dtype=int)))
        missingEdges[count] = len(adjMatrix) + 1 - nodesBelow - nodesAbove
        count += 1

def checkCompletion():
    #return true if graph is fully sorted
    global missingEdges
    return 0 == sum(missingEdges)

#def chooseLessKnow(number):
#    #simple heuristic to choose vertices for selection, just get all the vertices
#    #that have less edges on the graph
#    global adjMatrix
#    global missingEdges
#    ret = heapq.nlargest(number, range(len(missingEdges)), missingEdges.__getitem__)
#    return ret

def chooseRandom(number):
    global adjMatrix
    global missingEdges
    shuffled = range(len(missingEdges))
    random.shuffle(shuffled)
    ret = []
    count = 0
    index = 0
    while (count < number):
        if(index == len(shuffled) - 1):
            index = 0
            while (count < number):
                ret.append(shuffled[index])
                index += 1
                count += 1
            break
                
        if(missingEdges[shuffled[index]] == 0):
            index += 1
        else:
            ret.append(shuffled[index])
            count += 1
            index += 1
    return ret
            



def chooseLessKnow(number):
    global adjMatrix
    global missingEdges
    #need to shuffle to avoid skewed decision based on ordering
    #more complex heuristic that choose the first vertice that have less edges
    #and choose next vertices if they don't have a edge with the first one choosen
    shuffledList = missingEdges[:]
    shuffledIndex = range(len(shuffledList))
    random.shuffle(shuffledIndex)
    lSorted = heapq.nlargest(len(shuffledList), shuffledIndex, shuffledList.__getitem__)
    index = 0
    count = 0
    ret = []
    while(count < number):
        if(index == len(missingEdges)):
            while(count < number):
                ret.append(lSorted[count])
                count += 1
            break
        ret.append(lSorted[index])
        count += 1
        for i in lSorted[index + 1:]:
            if(count == number):
                break
            if(not isNeigh(lSorted[index],i)):
                ret.append(i)
                count += 1

        index += 1
    return ret

def choice(vertices):
    #performs the choice and graph updates
    choiceHandler(vertices)
    computeTransitive()
    updateMissingEdges()

def main():
    global adjMatrix
    global missingEdges
    #comand line parsing options
    parser = argparse.ArgumentParser(description='Numero de Vertices')
    parser.add_argument('numVertices', type=int,
            help='Numero de vertices no grafo necessario')
    parser.add_argument('verticesPerChoice', type=int,
            help='Numero de opcoes a cada escolha')
    args = parser.parse_args()

    
    #initialization
    verticesPerChoice = args.verticesPerChoice
    numVertices = args.numVertices
    adjMatrix = np.eye(numVertices, dtype=bool)
    missingEdges = []
    seen = dict()
    for i in range(numVertices):
        missingEdges.append(numVertices - i - 1)
    updateMissingEdges()

    #melhor case escolhendo um de cada 
    
    # choice([0,1,2])
    # choice([2,3,4])
    # choice([4,5,6])
    # choice([6,7,8])
    
    count = 0
    chooseFun = chooseRandom
    while(not checkCompletion()):
        offset = 1
        vertices = tuple(chooseFun(verticesPerChoice))
        while vertices in seen:
            #if the vertices have been used already
            vertices = chooseFun(verticesPerChoice + offset)
            random.shuffle(vertices)
            # newNum = vertices[verticesPerChoice + offset - 1]
            vertices = vertices[0:verticesPerChoice]
            # vertices.append(newNum)
            vertices.sort()
            vertices = tuple(vertices)
            offset += 1

        seen[vertices] = True
        choice(list(vertices))
        print(vertices)
        progress = sum(missingEdges)
        count += 1

    print(count)
    print(adjMatrix * 1)

 

main()
