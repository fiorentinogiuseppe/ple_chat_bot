import traceback
from .perguntador import Perguntar


class Chatbot:

    def __init__(self) -> None:
        self.__perguntadores = Perguntar.carregar_perguntadores()

    def perguntar(self, texto: str) -> str:
        resposta = ""
        for serv in self.__perguntadores:
            try:
                resultado = serv.verificar(texto)
                resposta = resultado
            except Exception as exp:
                print(traceback.print_exc())
                continue
        return resposta
