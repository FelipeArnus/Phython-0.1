arquivo = open('Memoria/arquivo.txt','w')


while True:
    x = int(input(': '))
    if x == 0:
        break
    arquivo.write(str(x) + '\n')

arquivo.close()
arquivo = open('Memoria/arquivo.txt', 'r')
print(arquivo.read())

arquivo.close()#fechar pq skin