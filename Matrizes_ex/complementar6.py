matrix = [[0,0,0][0,0,0][0,0,0]]
p = 'o'

def preenche_matriz(p):
    matrix = []
    for _ in range(3):
        if matrix[p]:
            linha = []
            for _ in range(3):
                x = int(input(': '))
                linha.append(x)
            matrix.append(linha)
    return matrix

def verf(matrix):
    print_matriz(matrix)
    v = int(input(f'Posição {p} formato é coluna e linha [][]:'))
    


def print_matriz(matrix):
    for c in range(len(matrix)):#coluna
        print()#skip coluna
        for l in range(len(matrix[0])):#linha
            print(matrix[c][l], end='\t')#no skip|linha

while True:

    while True:
        if v == 'x':
            v == 'o'
        elif v == 'o':
            v == 'x'
        print_matriz(matrix)
        p = int(input(f'Posição {v} formato é [coluna][linha]:'))
        preenche_matriz(p, v)


        v = verf(matrix)

    matrix = preenche_matriz()
    print_matriz(matrix)