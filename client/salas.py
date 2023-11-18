# o decorator de salas
# as salas devem ficar armazenadas dentro de um array
# esse array de salas deve ficar salvo em um arquivo .pickle
from dataclasses import dataclass

@dataclass
class Salas:
    salaNum: int=0
    programacao: list=''