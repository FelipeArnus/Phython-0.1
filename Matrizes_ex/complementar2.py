
def preenche_matriz():
    matrix = []
    for _ in range(5):
        linha = []
        for _ in range(5):
            x = int(input(': '))
            linha.append(x)
        matrix.append(linha)
    return matrix

def verifica(matrix):
    verf = ''
    for c in range(len(matrix)):#coluna
        print()#skip coluna
        for l in range(len(matrix[0])):#linha            
            if matrix[c][l] == matrix[l][c]:
                verf = 'É simetrico: '
            else:
                return ('Não é simetrico: ')
    return verf

def print_matriz(matrix, verf):
    print(f'{verf}')
    for c in range(len(matrix)):#coluna
        print()#skip coluna
        for l in range(len(matrix[0])):#linha
            print(matrix[c][l], end='\t')#no skip|linha


matrix = preenche_matriz()
verf = verifica(matrix)
print_matriz(matrix, verf)