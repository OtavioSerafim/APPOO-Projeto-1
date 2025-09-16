from Pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome:str, idade:int, numero_matricula:int):
        super().__init__(nome, idade)
        self.numero_matricula = numero_matricula
        self.notas = []
        
    def calcular_media_notas(self):
        soma = 0
        for nota in self.notas:
            soma = soma + nota
        return soma/len(self.notas)
            