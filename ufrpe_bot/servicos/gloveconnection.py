import os

from ufrpe_bot.servicos.singleton import Singleton
from gensim.models import KeyedVectors


@Singleton
class W2VConnection(object):
    _glove_path = os.getenv("GOVE_PATH")

    def __init__(self):
        self.model_glove = KeyedVectors.load_word2vec_format(self._glove_path, binary=False)

    def __str__(self):
        return self.model_glove
