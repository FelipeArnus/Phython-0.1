from random import randint

matriz = []
numeros_usados = []

def preencher_matriz_aleatoria(lin: int, col: int) -> list:
    matriz = []
    for i in range(lin):
        linha = []
        for j in range(col):
            while True:
                n = randint(1, 25)
                if n not in numeros_usados:
                    numeros_usados.append(n)
                    linha.append(n)
                    break
        matriz.append(linha)
    return matriz

def exibe_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end="\t")
        print()

matriz = preencher_matriz_aleatoria(5, 5)
exibe_matriz(matriz)
