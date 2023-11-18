import salas
import pickle

def validaOption(op):
    op = op.lower()
    if op in ['n', 's', 'd', 'p', 'e']:
        return True
    else:
        return False

def painel(user):
    print(f'\nOlá {user.name}.\n')
    
    print('Informações sobre as salas\n')
    ###
    try:
        with open('dadosSalas.pickle', 'rb') as file:
            salasCine = pickle.load(file)
    except:
        salasCine = []
    
    print(salasCine)

    if len(salasCine) > 0:
        for i in range(len(salasCine)):
            print(f' - Sala: {salasCine[i].salaNum};')
            print(f'   - Programação: {salasCine[i].programacao} \n')
    else:
        print('Nenhuma sala cadastrada ainda.')


    ## o adm deve ser capaz de cadastrar novas salas, excluir elas, e definir a programação daquela sala

    while True: 
        print('\n Menu de opções.')
        print(' Cadastrar nova sala [N] \n Exibir salas [E] \n Deletar salas [D] \n Definir a programação [P] \n Sair [S] \n')

        option = input('-> ')

        if validaOption(option) is not True:
            continue

        option = option.lower()

        if option == 's':
            break
        elif option == 'n':
            # pedir o numero da sala
            salaN = int(input('Número da sala: '))
            try:
                with open('dadosSalas.pickle', 'rb') as file:
                    dadosSalas = pickle.load(file)
            except:
                dadosSalas = []

            newSala = salas.Salas(salaN)
            dadosSalas.append(newSala)
            with open('dadosSalas.pickle', 'r+b') as file:
                pickle.dump(dadosSalas, file)
            continue

        elif option == 'e':
            try:
                with open('dadosSalas.pickle', 'rb') as file:
                    dadosSalas = pickle.load(file)
            except:
                dadosSalas = []


            if len(dadosSalas) > 0:
                for i in range(len(dadosSalas)):
                    print(f' - Sala: {dadosSalas[i].salaNum}; ')
                    print(f'   - Programação: {dadosSalas[i].programacao} \n')
            else:
                print('Nenhuma sala cadastrada ainda.')
            continue

        elif option == 'd':
            # pedir o numero da sala a ser deletado
            salaN = int(input('Número da sala: '))
            try:
                with open('dadosSalas.pickle', 'rb') as file:
                    dadosSalas = pickle.load(file)
            except:
                dadosSalas = []
            
            for i in range(len(dadosSalas)):
                if dadosSalas[i].salaNum == salaN:
                    dadosSalas.pop(i) # sala com o numero especificado foi deletada
                    with open('dadosSalas.pickle', 'r+b') as file:
                        pickle.dump(dadosSalas, file)
                    print(f'Sala {salaN} deletada.')
                    break
            continue

        elif option == 'p':
            # [nomeDoFilme, horario]
            salaN = int(input('Número da sala: '))
            try:
                with open('dadosSalas.pickle', 'rb') as file:
                    dadosSalas = pickle.load(file)
            except:
                dadosSalas = []

            flag = False
            index = 0
            for i in range(len(dadosSalas)):
                if dadosSalas[i].salaNum == salaN:
                    index = i
                    flag = True
            if flag:
                nomeDoFilme = input('Inserir nome do filme: ')
                horario = input('Inserir horario: ')

                dadosSalas[index].programacao += f' [{nomeDoFilme}, {horario}]'

                with open('dadosSalas.pickle', 'r+b') as file:
                    pickle.dump(dadosSalas, file)
                print('Programação definida com sucesso.')
            else:
                print('Sala não encontrada.')
            continue

    return False


