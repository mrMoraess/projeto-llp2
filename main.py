# main file

# primeira tela vai ser a de registro, podendo ser alterada para login
# deve haver a possibilidade de alterar para registro ou login de adm
import userLogin
import userRegist
import re

# primeiro vou chamar o userRegist e o userLogin

def validaOption(op):
    op = op.lower()
    if op == 'login' or op == 'registrar':
        return True
    else:
        return False
    
# essa function vai identificar o tipo do usuario, se ele e adm ou cliente
def identificaUser(user):
    if hasattr(user, 'admKey'):
        return ['adm']
    else:
        return ['client']
    
# nessa function vou definir se o usuario e adm ou cliente 
# depois vou direciona-lo para o seu painel especifico
def painel(user):
    userTipo = identificaUser(user)

    if userTipo[0] == 'adm':
        # aqui vou chamar a function painel do adm
        ...
    else:
        # e aqui vou chamar o painel do cliente
        ...

while True:
    print('\n REGISTRE UM NOVO USUÁRIO OU FAÇA LOGIN. \n')
    print(' Digite "login" ou "registrar", caso queira encerrar o programa digite "sair".')
    option = input('-> ')

    if option.lower() == 'sair':
        break

    if validaOption(option) is not True:
        print('\n Opção inválida, tente novamente.\n')
        continue

    if option == 'login':
        login = userLogin.login()
        if login is not True: # a def login vai retornar false quando o user cancelar o login
            continue
        else: 
            painel(login[1])
    else:
        userRegist.regist()
        if login is not True: # a def login vai retornar false quando o user cancelar o login
            continue
        else: 
            painel(login[1])