# aqui vou validar a key do adm
import re

def admKey(key):
    regex = '^[0-9]{6}$'
    return re.match(regex, key) is not None