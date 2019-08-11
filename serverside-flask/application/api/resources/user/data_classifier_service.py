import pandas as pd, numpy as np
from application.api.resources.user.dataset_util import DatasetUtil
from application.api.resources.user.datacleaner_service import DataCleanerService
from application.loader_proper_classification_singleton import LoaderPropertiesClassificationSingleton
import re, string
import os

class DataClassifierService:

    def classficandoTemp(content_list):
        s1 = LoaderPropertiesClassificationSingleton.instance()        

        obj = {'content': [i for i in content_list]}
        test = pd.DataFrame(data=obj)

        # test = DataCleanerService.clear_data(test)


        # eliminando vazios
        CONTENT = 'content'
        test[CONTENT].fillna("unknown", inplace=True)      

        # vetorizando com tf-idf
        vect = s1.vec

        # criando matriz esparca de numeros
        test_term_doc = vect.transform(test[CONTENT])

        x = s1.trn_term_doc
        test_x = test_term_doc

        label_cols = s1.label_cols
        train = s1.train

        preds = np.zeros((len(test), len(label_cols)))
        for i, j in enumerate(label_cols):
            m,r = DatasetUtil.get_mdl(x, train[j])
            preds[:,i] = m.predict_proba(test_x.multiply(r))[:,1]
    
        submid = pd.DataFrame({'content': test["content"]})
        submission = pd.concat([submid, pd.DataFrame(preds, columns = label_cols)], axis=1)
        
        return submission