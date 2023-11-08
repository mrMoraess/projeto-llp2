# senha deve conter no minimo 8 caracteres
# senha deve conter no maximo 32 caracteres
import re

def validPass(passW):
    regex = '^[a-zA-Z0-9.<>;:/?\[\]\\+=\-_*&%$#@!\^]{8,64}$'
    return re.match(regex, passW) is not None
    
# test
print(validPass('matsssssssssssssssssssssssssssssssssssssssssssssss'))

