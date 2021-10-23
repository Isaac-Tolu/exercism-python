from collections import Counter
from string import punctuation

PUNC = ''.join(punctuation.split("'"))

def count_words(sentence):

    for punc in PUNC:
        sentence = sentence.replace(punc, ' ')

    word_list = [word.strip("'") for word in sentence.lower().split()]

    return dict(Counter(word_list))