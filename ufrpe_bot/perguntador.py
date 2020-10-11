from abc import ABC, abstractmethod


class Perguntar(ABC):
    __registro = []

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.__registro.append(cls)

    @abstractmethod
    def verificar(self, pergunta: str) -> str:
        ...

    @classmethod
    def carregar_perguntadores(cls):
        for perguntadores_cls in cls.__registro:
            yield perguntadores_cls()
