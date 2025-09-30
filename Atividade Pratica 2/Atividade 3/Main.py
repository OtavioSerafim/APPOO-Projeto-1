from Jogadores import Atacantes, Goleiros
from Olheiro import Olheiro

def analisar_jogadores(olheiro: Olheiro, jogadores: list) -> None:
    for jogador in jogadores:
        print(f"\nAvaliação de {jogador.nome}:")
        olheiro.checar_media(jogador)
        olheiro.checar_max(jogador)
        olheiro.checar_min(jogador)

def main() -> None:
    
	atacante1 = Atacantes("Lucas Alves", [2, 1, 0, 3, 1])
	atacante2 = Atacantes("Pedro Silva", [1, 2, 2, 1, 0])
	goleiro1 = Goleiros("Marcos Dias", [5, 4, 6, 3, 4])
	goleiro2 = Goleiros("Felipe Souza", [4, 5, 5, 4, 6])

	olheiro = Olheiro("Rafael")

	print("=== Relatório de Atacantes ===")
	analisar_jogadores(olheiro, [atacante1, atacante2])

	print("\n=== Relatório de Goleiros ===")
	analisar_jogadores(olheiro, [goleiro1, goleiro2])


main()