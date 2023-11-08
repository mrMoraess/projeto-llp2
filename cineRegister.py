# nesse file vou criar o registro onde vou armazenar a programacao de cada sala do cinema
# cada sala vai conter uma lista com a programacao especifica do dia
from dataclasses import dataclass

@dataclass
class SalaCine:
    nome: str=''
    programacao: list=[]

# example
sala1 = SalaCine('sala 01', [['Star Wars', 32, '19:30']])

