import admLogin as login 
import admRegist as regist

def validaOption(op):
    op = op.lower()
    if op == 'login' or op == 'registrar':
        return True
    else:
        return False

while True:
    print('\n TERMINAL DE ADMINISTRAÇÃO \n')

    option = input('Digite "login" para logar ou "registrar" para acessar o painel de adm: \n -> ')

    if option.lower() == 'sair':
        break

    if validaOption(option) is not True:
        print(validaOption(option))
        continue

    if option.lower() == 'login':
        log = login.login()
        if log is not True:
            continue
    else:
        reg = regist.registro()
        if reg is not True: 
            continue