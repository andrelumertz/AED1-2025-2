from abc import ABC, abstractmethod

class Animal(ABC):  # Herda de ABC pra ser abstrata
    @abstractmethod
    def fazer_som(self):  # Método abstrato
        pass  # Só diz que existe, mas não faz nada