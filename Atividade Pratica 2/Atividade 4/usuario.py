from artista import Artista
from interface import Interface

class Usuario(Interface):
    def __init__(self, nome):
        self.__nome = nome
        self.__playlist = []
        self.__artistas = []

    def cria_playlist(self, num_art):
        for i in range(num_art):
            nome_art = input(f"Digite o nome do artista {i+1}: ")
            self.__artistas[i] = Artista(nome_art)
            num_musicas = int(input("Insira o numero de músicas do seu artista: "))
            self.__artistas[i].recebe_musicas(num_musicas)
            self.__playlist.append(__artistas[i].musicas)

    def nome(self):
        return self.__nome