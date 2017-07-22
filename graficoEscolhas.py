import numpy as np
import matplotlib.pyplot as plt

# def qtdArestasNovas(n, d, x, posicaoN, posicaoD):
#     arestaDeVerticesNovos = (d - x)
#     return (posicaoN - 1)*(posicaoD - x) + (n - (posicaoN - 1)) * (posicaoD - x)

# def qtdArestasNovas(n, d, x, posicaoN, posicaoD):
#     return (posicaoD - x) * n + ( d - posicaoD)

def qtdArestasNovas(n, d, x, posicaoN, posicaoD):
    #todos os acima da posicao escolhida
    acimaEscolha = posicaoN * ((d - x) - posicaoD)
    #todos os abaixo da posicao escolhida
    abaixoEscolha = posicaoD * ((n - x) - posicaoN)
    #relacao do vertice que ja esta no ordenado com as outras escolhas
    rel = (d - x)
    return acimaEscolha + abaixoEscolha + rel


numEscolhas = 5
posicaoEscolha = range(0,numEscolhas,1)

#configs
posicaoTotal = 0
numOrdenados = 20


eixoY = map(lambda x: qtdArestasNovas(numOrdenados, numEscolhas, 1, posicaoTotal, x), posicaoEscolha)

plt.xlim(-1, numEscolhas)
plt.ylim(0, max(eixoY) + 1) 


plt.plot(posicaoEscolha, eixoY, 'bs')
plt.show()





