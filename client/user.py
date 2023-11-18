# unica utilidade desse arq e armazenar a class user
from dataclasses import dataclass

@dataclass
class UserClient:
    name: str=''
    email: str=''
    passW: str=''
    tickets: list='' # nessa lista vai ficar salvo os tickets que o user possui

@dataclass
class UserAdm:
    name: str=''
    email: str=''
    admKey: int=''

# tickets example
# myList = [[qtd, filme, horario], [2, 'Interestelar 2', '20:30']]