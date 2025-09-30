from typing import Type
from Interface import EstatisticaInterface

class Olheiro:
    def __init__(self, nome:str) -> None:
        self.nome = nome
    
    def checar_media(self, jogador:Type[EstatisticaInterface]) -> float:
        media = jogador.calcular_media()
        print(self.nome,' checou que a média de pontuação do jogador foi: ',media)
        return media
    
    def checar_max(self, jogador:Type[EstatisticaInterface]) -> int:
        max = jogador.calcular_max()
        print(self.nome,' checou que a pontuação máxima do jogador foi: ', max)
        return max

    def checar_min(self, jogador:Type[EstatisticaInterface]) -> int:
        min = jogador.calcular_min()
        print(self.nome,' checou que a menor pontuação do jogador foi: ', min)
        return min
