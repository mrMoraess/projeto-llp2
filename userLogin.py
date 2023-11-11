# vou receber os dados do user, valida-los e verificar se ele existe
# caso exista vou determinar se e adm ou cliente
# caso contrario envio uma msg de erro e retorna False
# esse modulo ira retornar apenas uma lista contendo a classificacao do user ['cliente'], ['adm']
import userDados
import validateFunctions.validateName as validName
import validateFunctions.validateEmail as validEmail
import validateFunctions.validatePass as validPass
import errorsMsg as error
import user 
import pickle

# a ideia e que essa funcao repita ate que o usuario digite dados validos para que o login seja efetuado
def login():
    usrDados = userDados.userDados()

    # functions de validacao

    validatedName = validName.validName(usrDados[0])
    validatedEmail = validEmail.validEmail(usrDados[1])
    validatedPass = validPass.validPass(usrDados[2])

    # bloco para verificar se tudo esta correto
    if validatedName and validatedEmail and validatedPass:
        # verifico se o user existe
        # se existe envio ele para o painel



        return True # deve retornar um array contendo True e o decorador
    else:
        if validatedName is not True:
            print(error.createNewError('Nome inválido.'))
            return login()
        elif validatedEmail is not True:
            print(error.createNewError('Email inválido.'))
            return login()
        elif validatedPass is not True:
            print(error.createNewError('Senha inválida.'))
            return login()