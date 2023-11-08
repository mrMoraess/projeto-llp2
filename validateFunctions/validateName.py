# receber um nome e valida-lo
# requisitos: possuir mais de 2 caracteres e nao ser composto por numeros
import re

def validName(name):
    name = name.replace(' ', '')
    if len(name) > 2 and name.isalpha():
        return True
    else:
        return False


# test
print(validName("Matheus Rodrigu3s")) 

print(re.findall("^[a-zA-Z]{3,}$", "Matheus"))
print(re.findall("^[a-zA-Z0-9._+=%$#]+[@][a-zA-Z0-9]+[.][a-z]+$", "matheus@gmail.com"))