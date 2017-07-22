import numpy as np
import random
import argparse
import math
import heapq

global adjMatrix
global missingEdges

def isNeigh(a, b):
    global adjMatrix
    if(a < b):
        return adjMatrix[a][b]
    else:
        return adjMatrix[b][a]

def choiceHandler(vertices):
    global adjMatrix
    size = len(vertices)
    vertices.sort()

    for i in vertices:
        for j in vertices[vertices.index(i):]:
            adjMatrix[i][j] = True

def computeTransitive():
    global adjMatrix
    #compute the transitive matrix using matrix multiplication

    dimension = len(adjMatrix)
    numberOfTimes = math.ceil(math.sqrt(dimension))

    for i in range(dimension):
        adjMatrix = np.dot(adjMatrix,adjMatrix)

def updateMissingEdges():
    global adjMatrix
    global missingEdges
    #this function iterates through the rows of the matrix
    #checking if the number is already complete(ordered), and updating
    #the list of that keeps track of how many missing edges each vertices has
    count = 0
    for row in adjMatrix:
        missingEdges[count] = len(adjMatrix) - (np.dot(adjMatrix[count], np.ones(len(adjMatrix), dtype=int)))
        count += 1

def checkCompletion():
    #return true if graph is fully sorted
    global missingEdges
    return 0 == sum(missingEdges)

def chooseLessKnow(number):
    global adjMatrix
    global missingEdges
    ret = heapq.nlargest(number, range(len(missingEdges)), missingEdges.__getitem__)
    return ret

def chooseLessKnowNoRepeat(number):
    global adjMatrix
    global missingEdges
    #need to shuffle to avoid skewed decision based on ordering
    shuffledList = missingEdges[:]
    lSorted = heapq.nlargest(len(shuffledList), range(len(shuffledList)), shuffledList.__getitem__)
    print(lSorted)
    index = 0
    count = 0
    while(count < number):
        if(index == len(missingEdges)):
            while(count < number):
                ret.append(lSorted[count])
                count += 1
            break
        ret = [lSorted[index]]
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

    #melhor case escolhendo um de cada 
    
    # choice([0,1,2])
    # choice([2,3,4])
    # choice([4,5,6])
    # choice([6,7,8])
    
    count = 0
    chooseFun = chooseLessKnow
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
        print(adjMatrix)
        progress = sum(missingEdges)
        count += 1

    print(count)
    print(adjMatrix * 1)


 

main()
