from Aluno import Aluno
from Professor import Professor

def main():
    aluno = Aluno("Roberto")
    professor = Professor("Fernando", "FOOO")

    professor.soliciteEstudo(aluno)
    
main()