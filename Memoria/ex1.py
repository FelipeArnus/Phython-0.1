#Abre o arquivo "nomegenerico.txt" 
arquivoIn = open('Memoria/nomegenerico.txt','w')
#w para inserir e substituir dados -> PARA SEMPRE
#a inserir sem substituir -> PARA SEMPRE
#r para olhar

for _ in range(5):
    x = int(input(': '))
    arquivoIn.write(str(x) + '\n')#transforma int em str e adicona uma quebra de linha

arquivoIn.close()                        #|fechar abertura antiga
arquivoIn = open('nomegenerico.txt', 'r')#|abrir nova abertura
print(arquivoIn.read())                  #|diverfun

arquivoIn.close()#fechar pq skin