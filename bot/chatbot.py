from bot import Perguntar
import traceback


class Chatbot:

    def __init__(self) -> None:
        self.perguntadores = Perguntar.carregar_perguntadores()

    def perguntar(self, pergunta: str) -> str:
        resposta = ""
        for perguntar in self.perguntadores:
            try:
                resultado = perguntar.verificar(pergunta)
                resposta = resultado
            except Exception as exp:
                print(traceback.print_exc())
                continue
        return resposta
