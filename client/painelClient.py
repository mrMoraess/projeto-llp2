# esse modulo vai conter todas as funcionalidades disponiveis para o client
import pickle
import re

# primeiramente deve mostrar uma lista com os filmes que vai ser exibidos 
# contendo sala, titulo do filme, horario de exibicao e numero de assentos disponiveis
# o usuario deve ter as seguintes opcoes
# 1 - comprar ticket de determinado filme, quantos quiser de acordo com a disponibilidade
# 2 - alterar seus dados cadastrais
# 3 - excluir sua conta
# 4 - sair da conta

def validaOption(op):
    op = op.lower()
    if op in ['c', 's']:
        return True
    else:
        return False

def painel(user):
    print(f'\n Bem vindo {user.name}!\n')
    print(f'Seus tickets: \n')

    print(f'    - {user.tickets}')
    
    print('\n >>>> Opções de Filmes <<<< \n')

    try: 
        with open('dadosSalas.pickle', 'rb') as file:
            salas = pickle.load(file)
    except:
        salas = []

    # vou apresentar a ele opções de filmes 
    for i in range(len(salas)):
        print(f' - Sala: {salas[i].salaNum};')
        print(f'    - Programação: {salas[i].programacao} \n')
    

    # opcoes do usuario
    while True:
        print('Comprar tickets [C]\nSair [s]\n')
        option = input('-> ')
        option = option.lower()

        if validaOption(option) is not True:
            continue
        
        if option == 's':
            break
        elif option == 'c':
            salaN = int(input('Digite o número da sala: '))
            filmeOp = input('Digite o nome do filme: ')

            try: 
                with open('dadosSalas.pickle', 'rb') as file:
                    salas = pickle.load(file)
            except:
                salas = []

            if filmeOp in salas[salaN - 1].programacao:
                qtd = int(input('Quantidade de tickets: '))
                user.tickets += f' [Filme: {filmeOp}, Quantidade: {qtd}]'
            else:
                print('Filme ou sala não encontrado')
                continue
            
            with open('dadosClient.pickle', 'rb') as file:
                clients = pickle.load(file)

            index = 0
            for i in range(len(clients)):
                if clients[i].name == user.name and clients[i].email == user.email:
                    index = i
            
            # clients.pop(i)
            print(user.tickets)
            clients[index].tickets = user.tickets
            with open('dadosClient.pickle', 'r+b') as file:
                pickle.dump(clients, file)
            print('Compra do ticket efetuada com sucesso!')

    return False

    # vou ter que importar dados do adm para ter acesso aos dados das salas de filmes

