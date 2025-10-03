from artista import Artista
from interface import Interface

class Usuario(Interface):
    def __init__(self, nome):
        try:
            if not isinstance(nome, str):
                raise ValueError("O nome deve ser uma string")
        except ValueError as e:
            print(f"Erro ao criar usuário: {e}!")
        except:
            print("Erro inesperado ao instanciar Usuário!")

        self.__nome: str = nome
        self.playlist = []
        self.artistas = []

        self.num_art: int = int(input("Insira quantos artistas há na sua playlist: "))
        while(not isinstance(self.num_art, int) or isinstance(self.num_art, bool) or self.num_art <= 0):
            self.num_art = int(input("O número de artistas deve ser um inteiro maior que 0: "))


    def cria_playlist(self):
        for i in range(self.num_art):
            nome_art = input(f"Digite o nome do artista {i+1}: ")
            self.artistas.append(Artista(nome_art))
            self.playlist.append(self.artistas[i].musicas)

    @property
    def nome(self):
        return self.__nome