from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    def __init__(self, num_lados):
        self.num_lados = num_lados
        self.lados = []

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass

    def le_lados(self):
        for i in range(self.num_lados):
            self.lados.append(int(input(f"Insira o tamanho do lado {i+1} :")))

    def mostra_lados(self):
        for i in range(self.num_lados):
            print(self.lados[i], " ")
