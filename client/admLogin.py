import pickle
import admDados
import validateFunctions.validateName as validateName
import validateFunctions.validateEmail as validateEmail
import validateFunctions.admKeyValidate as admKey
from painelAdm import painel
from errorsMsg import createNewError
import user

def login():
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
                print('Usuário encontrado, efetuando login.')
                index = i
                flag = True

        if flag:
            painel(dadosAdm[index])
        else:
            print('Usuário inexistente ou inválido.')
            return False

    else: 
        if validatedName is not True:
            print(createNewError('Nome inválido'))
        elif validatedEmail is not True:
            print(createNewError('Adm inválido'))
        elif validatedKey is not True:
            print(createNewError('Key inválido'))
        
    return False