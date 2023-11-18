import pickle
import admDados
import validateFunctions.validateName as validateName
import validateFunctions.validateEmail as validateEmail
import validateFunctions.admKeyValidate as admKey
from painelAdm import painel
from errorsMsg import createNewError
import user

def registro():
    dados = admDados.admDados(1)
    print(dados)

    # todas essas functions devem retornar true or false
    validatedName = validateName.validName(dados[0])
    validatedEmail = validateEmail.validEmail(dados[1])
    validatedKey = admKey.admKey(dados[2])

    if validatedName and validatedEmail and validatedKey:

        try:
            with open('dadosAdm.pickle', 'rb') as file:
                dadosAdm = pickle.load(file)
        except:
            dadosAdm = []

        print(dadosAdm)

        index = 0
        flag = False
        for i in range(len(dadosAdm)):
            if dadosAdm[i].name == dados[0] and dadosAdm[i].email == dados[1] and dadosAdm[i].admKey == dados[2]:
                print('Os dados informados anteriormente já correspondem a uma conta. Será redirecionado para o painel dessa conta.')
                index = i
                flag = True

        newAdm = user.UserAdm(dados[0], dados[1], dados[2])

        if flag:
            painel(dadosAdm[index])
        else:
            dadosAdm.append(newAdm)
            print('Novo Adm cadastrado com sucesso. ')
            with open('dadosAdm.pickle', 'r+b') as file:
                pickle.dump(dadosAdm, file)
            return False

    else: 
        if validatedName is not True:
            print(createNewError('Nome inválido'))
        elif validatedEmail is not True:
            print(createNewError('Adm inválido'))
        elif validatedKey is not True:
            print(createNewError('Key inválido'))
    

    return False