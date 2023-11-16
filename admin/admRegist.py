import pickle
import admDados as dados
from ..client.validateFunctions.validateEmail import validEmail
from ..client.validateFunctions.validateName import validName
from ..client.validateFunctions.admKeyValidate import admKey
from ..client.errorsMsg import createNewError

def registro():
    dados = dados.admDados()

    # todas essas functions devem retornar true or false
    validatedName = validName(dados[0])
    validatedEmail = validEmail(dados[1])
    validatedKey = admKey(dados[2])

    if validatedName and validatedEmail and validatedKey:
        ...
    else: 
        if validatedName is not True:
            print(createNewError('Nome inválido'))
        elif validatedEmail is not True:
            print(createNewError('Adm inválido'))
        elif validatedKey is not True:
            print(createNewError('Key inválido'))