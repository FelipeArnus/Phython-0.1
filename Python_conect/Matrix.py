def preenche_matriz(a,b):
    matrix = []
    for _ in range(a):
        linha = []
        for _ in range(b):
            x = int(input(': '))
            linha.append(x)
        matrix.append(linha)
    return matrix

def print_matriz(matrix):
    #imprime
    for c in range(len(matrix)):#coluna
        print()#skip coluna
        for l in range(len(matrix[0])):#linha
            print(matrix[c][l], end='\t')#no skip|linha
