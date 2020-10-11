import random
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import re
from unidecode import unidecode
from ufrpe_bot.servicos.gloveconnection import W2VConnection
from ufrpe_bot.servicos.documentoOficial import LoadDocumentoOficial

word2vec_model = W2VConnection.Instance().__str__()
documento_oficial = LoadDocumentoOficial.Instance().__str__()


def uniqueid():
    seed = random.getrandbits(32)
    while True:
        yield seed
        seed += 1


def avg_sentence_vector(words, model, num_features, index2word_set):
    # function to average all words vectors in a given paragraph
    featureVec = np.zeros((num_features,), dtype="float32")
    nwords = 0

    for word in words:
        if word in index2word_set:
            nwords = nwords + 1
            featureVec = np.add(featureVec, model[word])

    if nwords > 0:
        featureVec = np.divide(featureVec, nwords)
    return featureVec


def clear_text(text):
    stopwords = nltk.corpus.stopwords.words('portuguese')
    u = unidecode(text)
    text_cleaned = re.sub(r"[^a-zA-Z ]", "", u)
    text_list = text_cleaned.split(" ")

    cleaned_list = [w.lower() for w in text_list if w.lower() not in stopwords and w.lower()]

    return ' '.join(cleaned_list)


def compare(contextos, quesito):
    maxx = 0
    text = ""
    for k, v in contextos.items():
        for kk, vv in v.items():
            for vvv in vv:
                cleanded_1 = clear_text(vvv)
                sentence_1_avg_vector = avg_sentence_vector(cleanded_1, model=word2vec_model, num_features=50,
                                                            index2word_set=set(word2vec_model.index2word))
                sentence_2_avg_vector = avg_sentence_vector(quesito, model=word2vec_model, num_features=50,
                                                            index2word_set=set(word2vec_model.index2word))
                sen1_sen2_similarity = \
                    cosine_similarity(sentence_1_avg_vector.reshape(1, -1), sentence_2_avg_vector.reshape(1, -1))[0][0]
                if sen1_sen2_similarity > maxx:
                    maxx = sen1_sen2_similarity
                    text = cleanded_1
    return maxx, text


def similaridade_contexto(q):
    _, contexto = compare(documento_oficial, q)
    return contexto
