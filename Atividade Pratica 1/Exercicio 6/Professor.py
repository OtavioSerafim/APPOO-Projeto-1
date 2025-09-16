from Pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome:str, idade:int, numero_turmas):
        super().__init__(nome, idade)
        self.numero_turmas = numero_turmas

    def lancar_nota(self, aluno, nota):
        aluno.notas.append(nota)