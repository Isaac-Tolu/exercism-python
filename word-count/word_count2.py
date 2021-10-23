from collections import Counter
from string import punctuation

PUNC = ''.join(punctuation.split("'"))

def count_words(sentence):

    translate_table = sentence.maketrans(PUNC, ' ' * len(PUNC))
    new_sentence = sentence.translate(translate_table)

    word_list = [word.strip("'") for word in new_sentence.lower().split()]
    count_dict = dict(Counter(word_list))
    
    return count_dict