import numpy as np

from ufrpe_bot import Perguntar
from ufrpe_bot.servicos import bertQA
from ufrpe_bot.utils.utils import similaridade_contexto, uniqueid


class BertQA(Perguntar):  # noqa

    model = bertQA.QuestionAnswering.Instance().__str__()

    def model_data(self, q):
        unique_sequence = uniqueid()
        return {
            "context": similaridade_contexto(q),
            'qas': [{
                'id': str(next(unique_sequence)),
                'is_impossible': True,
                'question': q,
                'answers': [{
                    'text': '',
                    'answer_start': 0
                }]
            }]
        }

    def verificar(self, pergunta: str) -> str:
        to_predict = np.asarray([self.model_data(pergunta)])
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
