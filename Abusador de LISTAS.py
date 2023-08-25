nomes = []
idades = []

while True:
    nome = input('Nome: ')
    if nome == '':
        break
    idade = int(input('Sapoha1: '))
    nomes.append(nome)
    idades.append(idade)
print(nomes)
print(idades)

for indice in range(len(idades)):
    if idades[indice] >= 18:
        print(nome[indice], idades[indice])
