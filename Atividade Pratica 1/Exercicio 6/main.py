from Professor import Professor
from Aluno import Aluno

def main():
    professor = Professor("Wagner Meira", 55, 3)
    aluno1 = Aluno("Germano", 21, 2023060839)
    aluno2 = Aluno("Ana", 20, 2023000001)

    professor.lancar_nota(aluno1, 8.5)
    professor.lancar_nota(aluno1, 7.0)
    professor.lancar_nota(aluno2, 9.0)

    print(f"Professor: {professor.nome}, idade: {professor.idade}, turmas: {professor.numero_turmas}")
    print(f"Aluno 1: {aluno1.nome}, matrícula: {aluno1.numero_matricula}, notas: {aluno1.notas}")
    print(f"Aluno 2: {aluno2.nome}, matrícula: {aluno2.numero_matricula}, notas: {aluno2.notas}")

    print(f"Média de {aluno1.nome}: {aluno1.calcular_media_notas():.2f}")
    print(f"Média de {aluno2.nome}: {aluno2.calcular_media_notas():.2f}")

    aluno1.chorar()
    professor.chorar()

if __name__ == "__main__":
    main()