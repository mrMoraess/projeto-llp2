# main file

# primeira tela vai ser a de registro, podendo ser alterada para login
# deve haver a possibilidade de alterar para registro ou login de adm
import userLogin
import userRegist
import painelAdm
import painelClient

# primeiro vou chamar o userRegist e o userLogin

def validaOption(op):
    op = op.lower()
    if op == 'login' or op == 'registrar':
        return True
    else:
        return False
    
# essa function vai identificar o tipo do usuario, se ele e adm ou cliente
def identificaUser(user):
    print('chamada')

    if hasattr(user, 'admKey'):
        return ['adm']
    else:
        print('cliente')
        return ['client']
    
# nessa function vou definir se o usuario e adm ou cliente 
# depois vou direciona-lo para o seu painel especifico
def painel(user):
    userTipo = identificaUser(user)

    if userTipo[0] == 'adm':
        # aqui vou chamar a function painel do adm
        painelAdm.painel(user)
    else:
        # e aqui vou chamar o painel do cliente
        painelClient.painel(user)

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
        login = userLogin.login() # a function login e regist retorna o decorator com os dados do user
        if login: # a def login vai retornar false quando o user cancelar o login
            painel(login[1])
        else: 
            continue
    else:
        regist = userRegist.regist()
        print('terminou o registro')
        print(regist)
        if regist: # a def login vai retornar false quando o user cancelar o login
            print('chamou o painel')
            painel(regist[1])
        else: 
            continue
