# email deve conter o seguinte formato: exemplo@mail.com
# qualquer coisa fora do padrao mencionado anteriormente sera invalida
import re

def validEmail(email):
    regex = '^[a-zA-Z0-9._+=%$#]+[@][a-zA-Z0-9]+[.][a-z]+$'
    return re.match(regex, email) is not None

# test
print(validEmail('Matheusmatheus.com'))