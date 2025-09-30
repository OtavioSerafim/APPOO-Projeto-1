from abc import ABC, abstractmethod

class EstatisticaInterface(ABC):
    @abstractmethod
    def calcular_media(self) -> float:
        pass

    @abstractmethod
    def calcular_max(self) -> int:
        pass

    @abstractmethod
    def calcular_min(self) -> int:
        pass
