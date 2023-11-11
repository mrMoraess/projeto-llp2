# vou receber os dados do usuario e valida-los
# depois vou registrar ele
import userDados
import validateFunctions.validateName as validateName
import validateFunctions.validateEmail as validateEmail
import validateFunctions.validatePass as validatePass
import errorsMsg as error
import user
import pickle

# a ideia e que essa funcao repita ate que o usuario digite dados validos para que o registro seja efetuado
def regist():
    usrDados = userDados.userDados()

    # functions de validacao 
    validName = validateName.validName(usrDados[0])
    validEmail = validateEmail.validEmail(usrDados[1])
    validPass = validatePass.validPass(usrDados[2])

    if validName and validEmail and validPass:
        # caso os dados sejam todos validos, registrar user no banco de dados
        # verificar se o user ja existe, caso sim encaminha-lo para seu painel
        print('tudo true')
        return [True, {}]
    else:
        if validName != True:
            print(error.createNewError('Nome inválido.'))
            return regist()
        elif validEmail != True:
            print(error.createNewError('Email invállido.'))
            return regist()
        elif validPass != True:
            print(error.createNewError('Senha inválida.'))
            return regist()