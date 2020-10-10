import os

from bot.servicos.singleton import Singleton
from simpletransformers.question_answering import QuestionAnsweringModel


@Singleton
class QuestionAnswering(object):
    _model_path = os.getenv("MODEL_PATH")
    _model_type = os.getenv("MODEL_TYPE")

    def __init__(self):
        self.model = QuestionAnsweringModel(self._model_type, self._model_path)
        self.model.lazy_loading = True

    def __str__(self):
        return self.model

