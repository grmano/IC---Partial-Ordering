import numpy as np
import matplotlib.pyplot as plt
import random
import argparse
import math
import heapq
import time
import graphUtils as gu
from transitiveClosure import transitiveClosure

global adjMatrix
global missingEdges
global memoChoose

def isNeigh(a, b):
    #since it a directed graph, to test if two vertices are neighbours
    #they have to be "sorted"
    global adjMatrix
    if(a < b):
        return adjMatrix[a][b]
    else:
        return adjMatrix[b][a]

def choiceHandler(vertices):
    #Updates adjMatrix with the edges from comparison
    global adjMatrix
    size = len(vertices)
    vertices.sort()

    for i in vertices:
        for j in vertices[vertices.index(i):]:
            adjMatrix[i][j] = True

def computeTransitive():
    global adjMatrix
    #Naive way
    #Using matrix multiplication
    #PS: Better method for this problem implemented in transitiveClosure.py


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
    #equivalent of having a topological sort with no ambiguity
    global missingEdges
    return 0 == sum(missingEdges)

def chooseRandom(number):
    #Random heuristic to be used as a base case in comparison
    #with better ones
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

def chooseMaxSetRandom(number):
    #Selects independent sets to be possible choices
    global adjMatrix
    global missingEdges
    global memoChoose

    ret = []

    if(len(memoChoose) == 0):
        memoChoose = gu.randomMaxSet(adjMatrix, 100)
        #print(memoChoose)
        #print(adjMatrix * 1)

    for i in range(number):
        if(len(memoChoose) == 0):
            break
        else:
            temp = memoChoose.pop()
            if(missingEdges[temp] == 0):
                i -= 1
                next
            else:
                ret.append(temp)

    for j in range(number - len(ret)):
       rand = random.randint(0, len(adjMatrix) - 1)
       count = 0
       while((rand in ret or missingEdges[rand] == 0) and count < len(missingEdges)):
           count += 1
           rand = random.randint(0, len(adjMatrix) - 1)
       ret.append(rand)

    return ret

def chooseMaxSetLess(number):
    #Selects independent sets to be possible choices
    global adjMatrix
    global missingEdges
    global memoChoose

    ret = []

    if(len(memoChoose) == 0):
        memoChoose = gu.randomMaxSet(adjMatrix, 100)
        #print(memoChoose)
        #print(adjMatrix * 1)

    for i in range(number):
        if(len(memoChoose) == 0):
            break
        else:
            temp = memoChoose.pop()
            if(missingEdges[temp] == 0):
                i -= 1
                next
            else:
                ret.append(temp)

    ret.extend(chooseLessKnown(number-len(ret)))

    return ret

# def chooseMaxSetPure(number):
#     #Selects independent sets to be possible choices
#     global adjMatrix
#     global missingEdges
#     global memoChoose
#
#     ret = []
#
#     if(len(memoChoose) == 0):
#         #computes new independent set if none are available
#         memoChoose = gu.randomMaxSet(adjMatrix, 500)
#         #print(memoChoose)
#         #print(adjMatrix * 1)
#
#     for i in range(number):
#         if(len(memoChoose) == 0):
#             break
#         else:
#             temp = memoChoose.pop()
#             if(missingEdges[temp] == 0):
#                 i -= 1
#                 next
#             else:
#                 ret.append(temp)
#
#     while (len(ret) < number):
#         #add other independe
#
#     for j in range(number - len(ret)):
#        rand = random.randint(0, len(adjMatrix) - 1)
#        count = 0
#        while((rand in ret or missingEdges[rand] == 0) and count < len(missingEdges)):
#            count += 1
#            rand = random.randint(0, len(adjMatrix) - 1)
#        ret.append(rand)
#
#     ret.extend(chooseLessKnown(number-len(ret)))
#
#     return ret

def chooseLessKnown(number):
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
    #and transitive computation
    global adjMatrix
    choiceHandler(vertices)

    start = time.time()
    adjMatrix = transitiveClosure(adjMatrix)
    fin = time.time()
    rec = fin - start

    #CODE TO TEST IF MY TRANSITIVE CLOSURE IS CORRECT AND FASTER
    # start = time.time()
    # computeTransitive()
    # fin = time.time()
    # mult = fin - start
    #
    # print "Time for dynamic = %0.3f" % (rec * 1000.0)
    # print "Time for matrix mult = %0.3f" % (mult * 1000.0)
    # if ( not np.array_equal(m, adjMatrix)):
    #     print("False")
    #     sys.exit(0)
    updateMissingEdges()

def main():
    global adjMatrix
    global missingEdges
    global memoChoose
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
    memoChoose = []
    seen = dict()
    for i in range(numVertices):
        missingEdges.append(numVertices - i - 1)
    updateMissingEdges()


    print("""Choose choice function:
    1 - Random
    2 - Less Known Vertices First
    3 - Max Independent Sets + Random
    4 - Max Independent Sets + Less Know
    """)

    inp = input("Number:")

    print("Want to see the graph of edges added by partial ordering?")
    print("1 = Yes 0 = No")
    plotFlag = input("Plot?:")

    plotFlag = int(plotFlag)

    if (inp == 1):
        chooseFun = chooseRandom
    elif (inp == 2):
        chooseFun = chooseLessKnown
    elif (inp == 3):
        chooseFun = chooseMaxSetRandom
    elif (inp == 4):
        chooseFun = chooseMaxSetLess

    else:
        sys.exit(0)

    count = 0
    if plotFlag:
        #Initialize if plot is to be drawn
        progress = sum(missingEdges)
        edgesGained =[]

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
        print(vertices)
        choice(list(vertices))
        if plotFlag:
            temp = sum(missingEdges)
            edgesGained.append((progress - temp)/2)
            progress = temp
        count += 1

    
    print(count)
    print(adjMatrix * 1)
    if plotFlag:
        ind = range(0, count)
        plt.ylim(0, max(edgesGained)+ 2)
        plt.plot(ind,edgesGained, 'bs')
        plt.grid(True)
        plt.show()

main()
