from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome:str, idade:int, numero_matricula:int):
        super().__init__(nome, idade)
        self.numero_matricula = numero_matricula
        self.notas = []
        
    def calcular_media_notas(self):
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)
            