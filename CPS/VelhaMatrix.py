matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
player = 'Q'

def preenche_matriz(matrix, player):
    while True:
        try:
            coluna = int(input(f'Jogador {player}, digite a coluna (0, 1 ou 2): '))
            linha = int(input(f'Jogador {player}, digite a linha (0, 1 ou 2): '))

            if matrix[coluna][linha] == 0:
                matrix[coluna][linha] = player
                break
            else:
                print("Essa posição já está ocupada. Tente novamente.")
        except (ValueError, IndexError):
            print("Entrada inválida. Tente novamente.")

def print_matriz(matrix):
    for c in range(len(matrix)):
        print()
        for l in range(len(matrix[0])):
            print(matrix[c][l], end='\t')

while True:
    print_matriz(matrix)
    preenche_matriz(matrix, player)

    if player == 'X':
        player = 'Q'
    else:
        player = 'X'

    # Verificar se alguém ganhou (implemente sua lógica de vitória aqui)
    # Verificar se houve empate (implemente sua lógica de empate aqui)
