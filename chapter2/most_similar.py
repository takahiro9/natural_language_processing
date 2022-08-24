import sys
sys.path.append('..')
from common.functions import text_to_corpus, corpus_to_co_matrix, most_similar


text = 'you say goodbye and i say hello.'
corpus, word_to_id, id_to_word = text_to_corpus(text)
vocab_size = len(word_to_id)
C = corpus_to_co_matrix(corpus, vocab_size)

most_similar('you', word_to_id, id_to_word, C, top=5)