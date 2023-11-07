# senha deve conter no minimo 8 caracteres
# senha deve conter no maximo 32 caracteres

def validPass(passW):
    if len(passW) > 7 and len(passW) < 33:
        return True
    else:
        return False
    

