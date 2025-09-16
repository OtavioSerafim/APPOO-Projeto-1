from Quadrado import Quadrado
from Retangulo import Retangulo
from Triangulo import Triangulo

def main():
    r = Retangulo()
    q = Quadrado()
    t = Triangulo()

    print(r.calcular_area())
    print(r.calcular_perimetro())
    print(q.calcular_area())
    print(q.calcular_perimetro())
    print(t.calcular_area())
    print(t.calcular_perimetro())
    print(t.triangulo_retangulo())



if __name__ == "__main__":
    main()