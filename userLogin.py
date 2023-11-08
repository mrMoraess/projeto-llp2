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

usrDados = userDados.userDados()

# functions de validacao

validatedName = validName(usrDados[0])
validatedEmail = validEmail(usrDados[1])
validatedPass = validPass(usrDados[2])

# bloco para verificar se tudo esta correto
if validatedName and validatedEmail and validatedPass:
    # verifico se o user existe
    # se existe envio ele para o painel
    ...
else:
    if validatedName is not True:
        print(error('Nome inválido.'))
    elif validatedEmail is not True:
        print(error('Email inválido.'))
    elif validatedPass is not True:
        print(error('Senha inválida.'))
    