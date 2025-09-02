from Bolo import Bolo

def main():
    bolo1 = Bolo("Red Velvet", "Creme", "Vermelha", True)
    bolo2 = Bolo("Limão", "Leite Condensado", "Limão", False)

    bolo3Principal = Bolo("Red Velvet", "Creme", "Vermelha", False)

    print(f"""Cobertura bolo 1: {bolo1.temCobertura}
    Cobertura bolo 2: {bolo2.temCobertura}
    Cobertura bolo 3 da Classe: {bolo3Principal.temCobertura}""")

    bolo3Objeto = bolo1
    bolo3Objeto.temCobertura = False

    print(f"""Cobertura bolo 1: {bolo1.temCobertura}
    Cobertura bolo 2: {bolo2.temCobertura}
    Cobertura bolo 3 vindo do bolo 3: {bolo3Objeto.temCobertura}""")

main()