import numpy as np

from ufrpe_bot import Perguntar
from ufrpe_bot.servicos import bertQA



class BertQA(Perguntar):  # noqa

    model = bertQA.QuestionAnswering.Instance()

    def perguntar(self, pergunta: str) -> str:
        to_predict = np.asarray([pergunta])
        predict = self.model.predict(to_predict, n_best_size=1)
        prob = predict[1][0]['probability'][0]
        resp = predict[0][0]['answer'][0]

        """
        if prob < 0.8:
                    return "" # retornar paragrafo com maior similaridade #
                else:
                    return resp # tinha a resposta e a resposta
        """

        return resp




