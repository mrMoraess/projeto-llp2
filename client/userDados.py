def userDados(registroOuLogin):
    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    passW = ''
    if registroOuLogin == 1:
        passW = input('Crie uma senha: ')
    elif registroOuLogin == 2:
        passW = input('Digite sua senha: ')
    return [nome, email, passW]
