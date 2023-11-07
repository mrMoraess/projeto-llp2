# vou receber os dados do usuario e valida-los
# depois vou registrar ele
import userDados
import validateFunctions.validateName as validateName
import validateFunctions.validateEmail as validateEmail
import validateFunctions.validatePass as validatePass
import errorsMsg as error

usrDados = userDados.userDados()

# functions de validacao 
validName = validateName(usrDados[0])
validEmail = validateEmail(usrDados[1])
validPass = validatePass(usrDados[2])

if validName and validEmail and validPass:
    # caso os dados sejam todos validos, registrar user no banco de dados
    ...
else:
    if validName != True:
        print(error('Nome inválido.'))
    elif validEmail != True:
        print(error('Email invállido.'))
    elif validPass != True:
        print(error('Senha inválida.'))
