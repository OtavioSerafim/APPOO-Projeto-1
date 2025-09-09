from hamburgueria import Hamburgueria
from cliente import Cliente

def main():
    c1 = Cliente("alfredo", "x-beicon")
    h1 = Hamburgueria("baconbacon", 20)
    c1.pedeHamburguer(h1)


if __name__ == "__main__":
    main()