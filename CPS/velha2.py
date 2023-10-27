#CEP do chambrone 04671071
#Bingo
import random

jogadores = {}
cartelas = {}
nPartidas = 0

# Função para gerar cartelas aleatórias
def preencher_matriz_aleatoria():
    numeros_usados = []
    matriz = []

    for i in range(5):
        linha = []
        for j in range(5):
            while True:
                if j == 0:
                    n = random.randint(1, 15)
                    if n < 10:
                        n = '0' + str(n)
                if j == 1:
                    n = random.randint(16, 30)
                if j == 2:
                    n = random.randint(31, 45)
                if j == 3:
                    n = random.randint(46, 60)
                if j == 4:
                    n = random.randint(61, 75)

                if n not in numeros_usados:
                    numeros_usados.append(n)
                    linha.append(n)
                    break
        matriz.append(linha)
    return matriz

# Função para exibir as cartelas
def print_matriz(matrix):
    print()
    for c in range(len(matrix)):
        for l in range(len(matrix[0])):
            print(matrix[c][l], end='\t')
        print()
    print('-----------------------------------\n')

# Função para sortear números
def num_aleatorio(nPast):
    while True:
        n = random.randint(1, 75)
        if n not in nPast:
            nPast.add(n)
            return n

# Função para verificar se um jogador venceu
def verf(cartela):
    for c in range(5):  # Verifica nas linhas
        i = 0
        for l in range(5):
            if cartela[c][l] == 'XX':
                i += 1
                if i == 5:
                    return True

    for c in range(5):  # Verifica nas colunas
        i = 0
        for l in range(5):
            if cartela[l][c] == 'XX':
                i += 1
                if i == 5:
                    return True

    # Verifica na diagonal
    i = 0
    for c in range(5):
        if cartela[c][c] == 'XX':
            i += 1
            if i == 5:
                return True

    # Verifica na outra diagonal
    i = 0
    for c in range(5):
        if cartela[c][4 - c] == 'XX':
            i += 1
            if i == 5:
                return True

    return False
    
# Função principal do jogo
def jogo_de_bingo():
    global nPartidas
    nPast = set()
    nPartidas += 1  # Incrementa o contador de partidas

    while True:
        num_jogadores = int(input('Quantos jogadores vão jogar (1 a 5)? '))
        if 1 <= num_jogadores <= 5:
            break

    jogadores.clear()
    cartelas.clear()
    nPast.clear()  # Limpa o conjunto de números passados

    for i in range(num_jogadores):
        nome = input(f"Nome do Jogador {i + 1}: ")
        cartelas[nome] = preencher_matriz_aleatoria()
        print_matriz(cartelas[nome])

    while True:
        input("Pressione Enter para sortear: ")

        nNew = num_aleatorio(nPast)

        print(f"Número sorteado: {nNew}")

        for nome, cartela in cartelas.items():
            for item in cartela:
                if nNew in item:
                    item[item.index(nNew)] = 'XX'

            if verf(cartela):
                print(f"{nome} venceu na partida {nPartidas}!")
                with open("ranking.txt", "a") as ranking:
                    ranking.write(f"{nome} - Partida {nPartidas}\n")
                return

        for nome, cartela in cartelas:
            print(f"Cartela do Jogador {nome}:")
            print_matriz(cartelas[nome])

while True:
    jogo_de_bingo()
    novo_jogo = input("Deseja jogar novamente? (s/n): ")
    if novo_jogo.lower() == 'n':
        break
