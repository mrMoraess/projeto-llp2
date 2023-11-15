# vou receber os dados do usuario e valida-los
# depois vou registrar ele
import userDados
import validateFunctions.validateName as validateName
import validateFunctions.validateEmail as validateEmail
import validateFunctions.validatePass as validatePass
import errorsMsg as error
import user
import pickle
import painelClient

# a ideia e que essa funcao repita ate que o usuario digite dados validos para que o registro seja efetuado
def regist():
    usrDados = userDados.userDados(1)

    # functions de validacao 

    validName = validateName.validName(usrDados[0])
    validEmail = validateEmail.validEmail(usrDados[1])
    validPass = validatePass.validPass(usrDados[2])

    if validName and validEmail and validPass:
        # caso os dados sejam todos validos, registrar user no banco de dados
        # verificar se o user ja existe, caso sim encaminha-lo para seu painel

        try:
            with open('dadosClient.pickle', 'rb') as file:
                dados = pickle.load(file)
        except:
            dados = []
        
        print(dados)

        flag = False
        index = 0
        for i in range(len(dados)):
            if dados[i].name == usrDados[0] and usrDados[1] == dados[i].email and usrDados[2] == dados[i].passW:
                print('\n Usuário já existente. \n')
                flag = True
                index = i
                break
        
        newUser = user.UserClient(usrDados[0], usrDados[1], usrDados[2])
        if flag:
            print(f'Usuário {newUser.name} já existe, será redirecionado para o seu respectivo painel. \n')
            painelClient.painel(dados[index])
            return False
        else:
            dados.append(newUser)
            print('\n Usuário registrado com sucesso. \n')
            with open('dadosClient.pickle', 'r+b') as file:
                pickle.dump(dados, file)

        print(dados)
        return [True, newUser]
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