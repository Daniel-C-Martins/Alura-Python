from abc import ABC, abstractmethod #Classe abstrata

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    def __str__(self):
        return self._nome
    
    @abstractmethod
    def aplicar_desconto(self):
        pass