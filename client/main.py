# main file

# primeira tela vai ser a de registro, podendo ser alterada para login
# deve haver a possibilidade de alterar para registro ou login de adm
import userLogin
import userRegist
import painelClient

# primeiro vou chamar o userRegist e o userLogin

def validaOption(op):
    op = op.lower()
    if op == 'login' or op == 'registrar':
        return True
    else:
        return False

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
            painelClient.painel(login[1])
        else: 
            continue
    else:
        regist = userRegist.regist()
        if regist: # a def login vai retornar false quando o user cancelar o login
            print('chamou o painel')
            painelClient.painel(regist[1])
        else: 
            continue
