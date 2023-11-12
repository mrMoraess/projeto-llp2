# aqui vou receber os dados que devem ser salvos 
# vou ter uma lista de clientes e adm
# esse modulo vai ser usado no login para salvar os dados 
import pickle

def save(userDados): # vou receber os dados do user
    with open('dadosClient.txt', 'rb') as file:
        dados = pickle.load(file)

    dados += userDados

    with open('dadosClient.txt', 'r+b') as file:
        pickle.dumps(dados, file)

# test
# while True:
#     name = input('-> ')
#     if name == '0':
#         break

#     with open('test.txt', 'rb') as file:
#         dados = pickle.load(file)

#     dados += name

#     with open('test.txt', 'r+b') as file:
#         pickle.dump(dados, file)