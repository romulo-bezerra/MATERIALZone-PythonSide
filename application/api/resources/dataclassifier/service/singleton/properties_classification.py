import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import re, string
import os

class PropertiesClassification:
    __instance = None    
    
    # carregando o dataset apartir do diretório de trabalho da aplicação 
    __workDir = os.getcwd()
    train = pd.read_csv(__workDir + r'/dataset-processed.csv')

    # inserindo rotulos
    label_cols = ['programacao orientada a objeto', 'linguagem de marcacao', 'banco de dados', 'linguagem de script']
    train['none'] = 1-train[label_cols].max(axis=1)

    # eliminando vazios
    CONTENT = 'content'
    train[CONTENT].fillna("unknown", inplace=True)

    # criando um saco de palavras
    def __tokenize(s): 
        re_tok = re.compile(f'([{string.punctuation}“”¨«»®´·º½¾¿¡§£₤‘’])')
        return re_tok.sub(r' \1 ', s).split()

    # vetorizando com tf-idf
    vec = TfidfVectorizer(ngram_range=(1,2), tokenizer=__tokenize, 
            min_df=3, max_df=0.9, strip_accents='unicode', 
                use_idf=1, smooth_idf=1, sublinear_tf=1)

    # criando matriz esparca de numeros
    trn_term_doc = vec.fit_transform(train[CONTENT]) 

    @staticmethod
    def instance():
        if not PropertiesClassification.__instance:
            PropertiesClassification.__instance = PropertiesClassification()
        return PropertiesClassification.__instance
