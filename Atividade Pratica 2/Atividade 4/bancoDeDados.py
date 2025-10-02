from artista import Artista
from usuario import Usuario

class BancoDeDados:
    def __init__(self):
        pass

    def processar_playlist(self, usuario: Usuario):
        with open("playlist.txt", "a") as f:
            for i in range(usuario.num_art):
                for j in range(len(usuario.playlist[i])):
                    f.write(f"'{usuario.playlist[i][j]}' de {usuario.artistas[i].nome}\n")
                    print(f"'{usuario.playlist[i][j]}' de {usuario.artistas[i].nome}")