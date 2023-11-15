# esse modulo vai conter todas as funcionalidades disponiveis para o client
import pickle

# primeiramente deve mostrar uma lista com os filmes que vai ser exibidos 
# contendo sala, titulo do filme, horario de exibicao e numero de assentos disponiveis
# o usuario deve ter as seguintes opcoes
# 1 - comprar ticket de determinado filme, quantos quiser de acordo com a disponibilidade
# 2 - alterar seus dados cadastrais
# 3 - excluir sua conta
# 4 - sair da conta

def painel(user):
    print(f'\n Bem vindo {user.name}!\n')
    print(f'Seus tickets: \n')

    # vou mostrar todos os tickets que o client possui
    for i in range(len(user.tickets)):
        print(f'   - {user.tickets[i]}') # tickets vai ser uma lista contendo nome do filme, sala e horario
    
    print('\n >>>> Opções de Filmes <<<< \n')

    # vou apresentar a ele opções de filmes 
    for i in range(len(salas)):
        print(f' - Sala: {salas[i].salaNum}; \n')
        for f in range(len(sala[i].programacao)):
            print(f'   - {sala[i].programacao[f]}')

    # vou ter que importar dados do adm para ter acesso aos dados das salas de filmes

