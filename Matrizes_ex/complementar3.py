from random import randint

matriz = []
numeros_usados = []

def preencher_matriz_aleatoria():
    matriz = []
    for i in range(7):
        linha = []
        for j in range(7):
            while True:
                n = randint(1, 50)
                if n not in numeros_usados:
                    numeros_usados.append(n)
                    linha.append(n)
                    break
        matriz.append(linha)
    return matriz

def exibe_matriz(matriz):
    for i in range(len(matriz)):
        print(max(matriz[i]))

def print_matriz(matrix):
    for c in range(len(matrix)):#coluna
        print()#skip coluna
        for l in range(len(matrix[0])):#linha
            print(matrix[c][l], end='\t')#no skip|linha
    print()
    print()

matriz = preencher_matriz_aleatoria()
print_matriz(matriz)
exibe_matriz(matriz)
