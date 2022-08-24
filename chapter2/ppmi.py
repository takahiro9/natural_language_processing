import sys
sys.path.append('..')
import numpy as np
from common.functions import text_to_corpus, corpus_to_co_matrix, most_similar, ppmi

text = 'you say goodbye and i say hello.'
corpus, word_to_id, id_to_word = text_to_corpus(text)
vocab_size = len(word_to_id)
C = corpus_to_co_matrix(corpus, vocab_size)
W = ppmi(C)

np.set_printoptions(precision=3)
print('covariance matrix')
print(C)
print('-'*50)
print('PPMI')
print(W)
