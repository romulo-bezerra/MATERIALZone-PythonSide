import pandas as pd
import nltk
import re
from collections import OrderedDict
import warnings
warnings.filterwarnings('ignore')

class DataCleanerService:

    def __normalize_to_lowercase(text):
        return text.lower()

    def __remove_punctuation_with_space(text):
        return re.sub('[^\w\s]', ' ', text)

    def __remove_numeration_with_null(text):
        return re.sub(r'\b\d+\b', '', text)

    def __tokenize(text):    
        return nltk.word_tokenize(text)   

    def __remove_stopwords_portuguese(list_text):
        stopwords_portuguese = nltk.corpus.stopwords.words('portuguese')
        meaningful_words = [w for w in list_text if not w in stopwords_portuguese]
        return (meaningful_words)

    def __remove_words_duplicates_inline(rows_text):
        # creates a key dictionary and returns only the keys in list format, 
        # [...] eliminating duplicates by maintaining the insertion order 
        duplicates_deleted = list(OrderedDict.fromkeys(rows_text).keys())
        return duplicates_deleted

    def __rejoin_words(row):
        joined_words = (" ".join(row))
        return joined_words

    def clear_data(text):
        text = DataCleanerService.__normalize_to_lowercase(text)
        text = DataCleanerService.__remove_punctuation_with_space(text)
        text = DataCleanerService.__remove_numeration_with_null(text)
        text = DataCleanerService.__tokenize(text)
        text = DataCleanerService.__remove_stopwords_portuguese(text)
        text = DataCleanerService.__remove_words_duplicates_inline(text)
        text = DataCleanerService.__rejoin_words(text)
        return text