class Aluno:
    def __init__(self, nome):
        self.nome = nome
    
    def estude(self, horas, materia, nome):
        print(f"O Aluno {self.nome} está estudando para a prova da disciplina {materia} por {horas}, horas, pois o professor {nome} o requisitou")

