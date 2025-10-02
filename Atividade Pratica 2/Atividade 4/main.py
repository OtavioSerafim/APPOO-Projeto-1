from usuario import Usuario
from bancoDeDados import BancoDeDados

def main():
    usuario1 = Usuario("Germano")
    usuario1.cria_playlist()

    bd = BancoDeDados()
    bd.processar_playlist(usuario1)

if __name__ == "__main__":
    main()