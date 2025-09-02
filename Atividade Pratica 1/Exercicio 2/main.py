from FazBolo import FazBolo

def main():
    bolo = FazBolo("chocolate", "morango", "granulado")
    print("\nCaso 1: 10 minutos em fogo alto")
    bolo.assar("alto", 10)
    print("\nCaso 2: 30 minutos em fogo médio")
    bolo.assar("médio", 30)
    print("\nCaso 3: 45 minutos em fogo baixo")
    bolo.assar("baixo", 45)
    print("\nCaso 4: 120 minutos em fogo alto")
    bolo.assar("alto", 120)
    print("\nCaso 5: 0 minutos em fogo médio")
    bolo.assar("médio", 0)
    print("\nCaso 6: 30 minutos em fogo auto")
    bolo.assar("auto", 30)
    print("\nCaso 7: -15 minutos em fogo médio")
    bolo.assar("médio", -15)
    print("\nCaso 8: 30 minutos em fogo alto")
    bolo.assar("alto", 30)
    print("\nCaso 9: 10 minutos em fogo baixo")
    bolo.assar("baixo", 30)
    
main()