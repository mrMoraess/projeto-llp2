# unica utilidade desse arq e armazenar a class user
from dataclasses import dataclass

@dataclass
class UserClient:
    name: str=''
    email: str=''
    passW: str=''

@dataclass
class UserAdm:
    name: str=''
    email: str=''
    passW: str=''
    admKey: int=0
