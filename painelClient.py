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
    print(f'\n Bem vindo f{user.name}!\n')