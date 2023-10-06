
with open('Memoria/nomegenerico.txt', 'r') as arquivo:
    soma = 0
    for linha in arquivo:
        print(linha, end='')
        soma += int(linha)

    print(f'Soma: {soma}')

    #não é necessario fazer o close