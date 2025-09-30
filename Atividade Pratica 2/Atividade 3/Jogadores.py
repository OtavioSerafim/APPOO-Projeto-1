from Interface import EstatisticaInterface

class Atacantes(EstatisticaInterface):
    def __init__(self, nome: str, gols: list):
        try:
            self.gols = gols
            self.nome = nome
        except Exception as e:
            print(f"Erro ao criar atacante: {e}")
    
    def calcular_media(self) -> float:
        soma = 0
        
        for gol in self.gols:
            soma = soma + gol
        
        return soma/len(self.gols)

    def calcular_max(self) -> int:
        return max(self.gols)

    def calcular_min(self) -> int:
        return min(self.gols)
        
        
    
class Goleiros(EstatisticaInterface):
    def __init__(self, nome: str, defesas: list):
        try:
            self.defesas = defesas
            self.nome = nome
        except Exception as e:
            print(f"Erro ao criar goleiro: {e}")
    
    def calcular_media(self) -> float:
        soma = 0
        
        for defesa in self.defesas:
            soma = soma + defesa
        
        return soma/len(self.defesas)

    def calcular_max(self) -> int:
        return max(self.defesas)

    def calcular_min(self) -> int:
        return min(self.defesas)