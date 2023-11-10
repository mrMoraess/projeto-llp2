# vou receber os dados do usuario e valida-los
# depois vou registrar ele
import userDados
import validateFunctions.validateName as validateName
import validateFunctions.validateEmail as validateEmail
import validateFunctions.validatePass as validatePass
import errorsMsg as error
import user

# a ideia e que essa funcao repita ate que o usuario digite dados validos para que o registro seja efetuado
def regist():
    usrDados = userDados.userDados()

    # functions de validacao 
    validName = validateName(usrDados[0])
    validEmail = validateEmail(usrDados[1])
    validPass = validatePass(usrDados[2])

    if validName and validEmail and validPass:
        # caso os dados sejam todos validos, registrar user no banco de dados
        # verificar se o user ja existe, caso sim encaminha-lo para seu painel
        return True
    else:
        if validName != True:
            print(error('Nome inválido.'))
            return regist()
        elif validEmail != True:
            print(error('Email invállido.'))
            return regist()
        elif validPass != True:
            print(error('Senha inválida.'))
            return regist()