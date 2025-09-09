class Professor:
    def __init__(self, nome, materia):
        self.nome = nome
        self.materia = materia
    
    def soliciteEstudo(self, aluno):
        horas = -1
        while True:
            try:
                horas = int(input("Digite o número de horas a serem estudadas: "))
                if (horas >= 0):
                    break
                else:
                    print("Digite um número positivo.")
            except:
                print("Digite um número válido")
                
        aluno.estude(horas, self.materia, self.nome)