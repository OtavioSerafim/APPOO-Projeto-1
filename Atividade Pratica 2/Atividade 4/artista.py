from interface import Interface

class Artista(Interface):
    def __init__(self, nome: str):
        try:
            if not isinstance(nome, str):
                raise ValueError("O nome deve ser uma string")
        except ValueError as e:
            print(f"Erro ao criar artista: {e}!")
        except:
            print("Erro inesperado ao instanciar Artista!")

        self.__nome: str = nome
        self.musicas = []


        self.num_musicas: int = int(input("Insira o número de músicas desse artista: "))
        while(not isinstance(self.num_musicas, int) or isinstance(self.num_musicas, bool) or self.num_musicas <= 0):
            self.num_musicas = int(input("O número de músicas deve ser um inteiro maior que 0: "))

        for i in range(self.num_musicas):
            self.musicas.append(input(f"Música {i+1}: "))


    @property
    def nome(self):
        return self.__nome