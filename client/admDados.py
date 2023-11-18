def admDados(registroOuLogin):
    nome = input('Digite seu nome: ')
    email = input('Digite seu email: ')
    admKey = ''
    if registroOuLogin == 1:
        admKey = input('Crie uma key de adm: ')
    elif registroOuLogin == 2:
        admKey = input('Digite sua key: ')
    return [nome, email, admKey]
