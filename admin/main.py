import admLogin as login 
# import admRegist as regist
from ..client.main import *

while True:
    print('\n TERMINAL DE ADMINISTRAÇÃO \n')

    option = input('Digite "login" para logar ou "registrar" para acessar o painel de adm: \n -> ')

    if validaOption.validaOption(option) is not True:
        print('uau')
        continue

    if option.lower() == 'login':
        login = login.login()
    else:
        ...
        # regist.registro()