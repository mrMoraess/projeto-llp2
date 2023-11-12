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
import painelClient

# a ideia e que essa funcao repita ate que o usuario digite dados validos para que o login seja efetuado
def login():
    # possibilidade do adm logar
    
    usrDados = userDados.userDados(2)

    # functions de validacao

    validatedName = validName.validName(usrDados[0])
    validatedEmail = validEmail.validEmail(usrDados[1])
    validatedPass = validPass.validPass(usrDados[2])

    # bloco para verificar se tudo esta correto
    if validatedName and validatedEmail and validatedPass:
        # verifico se o user existe
        # se existe envio ele para o painel

        try:
            with open('dadosClient.pickle', 'wb') as file:
                dados = pickle.load(file)
        except:
            dados = []
        
        flag = False
        index = 0
        for i in range(len(dados)):
            if dados[i].name == usrDados[0] and usrDados[1] == dados[i].email and usrDados[2] == dados[i].passW:
                print('\n Login efetuado com sucesso. \n')
                flag = True
                index = i
                break
        
        newUser = user.UserClient(usrDados[0], usrDados[1], usrDados[2])
        if flag:
            painelClient.painel(dados[index])
            return False
        else:
            dados.append(newUser)
            print('\n Usuário inexistente ou inválido. Você será redirecionado para o painel inicial, faça seu cadastro. \n')
            return False
        
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