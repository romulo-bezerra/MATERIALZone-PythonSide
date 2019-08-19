import pandas as pd, numpy as np
from application.api.resources.dataclassifier.util.dataset.dataset_util import DatasetUtil
from application.api.resources.dataclassifier.service.singleton.properties_classification import PropertiesClassification

class DataClassifierService:

    def rateContent(content_list):
        pc = PropertiesClassification.instance()

        obj = {'content': [i for i in content_list]}
        test = pd.DataFrame(data=obj)

        # eliminando vazios
        CONTENT = 'content'
        test[CONTENT].fillna("unknown", inplace=True)      

        # vetorizando com tf-idf
        vect = pc.vec

        # criando matriz esparca de numeros
        test_term_doc = vect.transform(test[CONTENT])

        x = pc.trn_term_doc
        test_x = test_term_doc

        label_cols = pc.label_cols
        train = pc.train

        preds = np.zeros((len(test), len(label_cols)))
        for i, j in enumerate(label_cols):
            m,r = DatasetUtil.get_mdl(x, train[j])
            preds[:,i] = m.predict_proba(test_x.multiply(r))[:,1]
    
        submid = pd.DataFrame({'content': test["content"]})
        submission = pd.concat([submid, pd.DataFrame(preds, columns = label_cols)], axis=1)
        
        return submission
