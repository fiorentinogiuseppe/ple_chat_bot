import os
import json
from ufrpe_bot.servicos.singleton import Singleton

@Singleton
class LoadDocumentoOficial(object):
    _doc_path = os.getenv("DOC_PATH")
    _qa_doc = []

    def __init__(self):
        with open(self._doc_path) as json_file:
            self._qa_doc = json.load(json_file)

    def __str__(self):
        return self._qa_doc

