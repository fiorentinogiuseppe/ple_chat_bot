import numpy as np

from ufrpe_bot import Perguntar
from ufrpe_bot.servicos import bertQA
from ufrpe_bot.utils.utils import similaridade_contexto, uniqueid


class BertQA(Perguntar):  # noqa

    model = bertQA.QuestionAnswering.Instance().__str__()

    def model_data(self, q):
        unique_sequence = uniqueid()
        contexto = similaridade_contexto(q)
        return contexto, {
            "context": contexto,
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
        contexto, dic = self.model_data(pergunta)
        to_predict = np.asarray([dic])
        predict = self.model.predict(to_predict, n_best_size=1)
        prob = predict[1][0]['probability'][0]
        resp = predict[0][0]['answer'][0]

        if prob < 0.8:
            return "Desculpe, mas não entendi muito bem. Contudo encontramos um paragrafo que pode tirar sua dúvida." \
                   "\n{}".format(contexto)
        else:
            return resp

