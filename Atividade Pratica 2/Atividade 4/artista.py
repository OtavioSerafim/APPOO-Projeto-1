from interface import Interface

class Artista(Interface):
    def __init__(self, nome):
        num_musicas = int(input("Digite o número de músicas do artista"))            
        self.__nome = nome
        self.musicas = []
        for i in range(num_musicas):
            self.musicas.append(input(f"Música {i+1}: "))

    @property
    def nome(self):
        return self.__nome