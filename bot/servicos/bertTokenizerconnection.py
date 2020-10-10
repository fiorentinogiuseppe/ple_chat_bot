import os

from bot.servicos.singleton import Singleton
from transformers import BertTokenizer

@Singleton
class BERTtConnection(object):
    _bert_path = os.getenv("BERT_PATH")

    def __init__(self):
        self.tokenizer = BertTokenizer.from_pretrained(self._bert_path)

    def __str__(self):
        return self.tokenizer

    def tokeniza(self, texto):
        return self.tokenizer.tokenize(texto)