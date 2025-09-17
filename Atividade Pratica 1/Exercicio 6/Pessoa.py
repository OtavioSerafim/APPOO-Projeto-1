class Pessoa():
    def __init__(self, nome: str, idade: int):
        self.nome = nome
        self.idade = idade
    
    def chorar(self):
        print(f"{self.nome} chorou bua bua bua!")