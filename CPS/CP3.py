rede_social = {'felps': {'nome': 'João Silva', 'idade': 23, 'amigos': ['chambs']},
               'chambs': {'nome': 'Maria Vieira', 'idade': 20, 'amigos': ['vic', 'felps']},
               'vic': {'nome': 'Karina Andrade', 'idade': 27, 'amigos': []}
               }

def menu():
    while True:
        print('\nO que você deseja fazer?')
        print('1 - Inserir um membro na lista')
        print('2 - Editar amigos de um usuário')
        print('3 - Printar amigos')
        print('4 - Sair')
        x = input('Digite a opção desejada: ')
        
        if x == '1':
            inserir_membro()
        elif x == '2':
            editar_amigos()
        elif x == '3':
            print_amigos()
        elif x == '4':
            break
        else:
            print('Opção inválida.')

def inserir_membro():
    try:
        chave = input('Digite a chave: ')
        nome = input('Digite o nome do usuário: ')
        idade = int(input('Digite a idade do usuário: '))

        amigos_validos = []

        rede_social[chave] = {'nome': nome, 'idade': idade, 'amigos': amigos_validos}
    except ValueError:
        print('Erro: Certifique-se de que a idade seja um número inteiro.')
    except Exception as e:
        print(f'Erro: Ocorreu um erro inesperado - {e}')
    menu()

def editar_amigos():
    try:
        nick = input('Digite a chave do usuário: ')
        if nick in rede_social:
            amigos_validos = rede_social[nick]['amigos']

            amigos = input('Digite os novos amigos do usuário separados por espaço: ').split()
            inimigos = input('Pessoas que você não quer na lista separadas por espaço: ').split()

            # Remove inimigos da lista de amigos
            for inimigo in inimigos:
                if inimigo in amigos_validos:
                    amigos_validos.remove(inimigo)
                else:
                    print(f'O membro "{inimigo}" não está na lista de amigos.')

            # Verifica se os amigos são chaves válidas na rede social e evita amigos repetidos
            for amigo in amigos:
                if amigo == nick:
                    print(f'Você não pode adicionar a si mesmo como amigo.')
                elif amigo in rede_social:
                    if amigo not in amigos_validos:
                        amigos_validos.append(amigo)
                    else:
                        print(f'O membro "{amigo}" já está na lista de amigos.')
                else:
                    print(f'O membro "{amigo}" não é um usuário válido.')

            rede_social[nick]['amigos'] = amigos_validos
            print(f'Amigos atualizados para {amigos_validos}')
        else:
            print('Usuário não encontrado.')
    except Exception as e:
        print(f'Erro: Ocorreu um erro inesperado - {e}')
    menu()

def print_amigos():
    try:
        nick = input('Digite a chave do usuário: ')
        if nick in rede_social:
            amigos = rede_social[nick]['amigos']
            print('Amigos de', nick, ':', amigos)
        else:
            print('Usuário não encontrado.')
    except Exception as e:
        print(f'Erro: Ocorreu um erro inesperado - {e}')
    menu()

menu()
