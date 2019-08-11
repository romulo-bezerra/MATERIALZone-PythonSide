from sklearn.linear_model import LogisticRegression
import pandas as pd, numpy as np

class DatasetUtil:
    # equacao basica de naive bayes
    def pr(x, y_i, y):
        p = x[y==y_i].sum(0)
        return (p+1) / ((y==y_i).sum()+1)

    def get_mdl(x,y):
        y = y.values
        r = np.log(DatasetUtil.pr(x,1,y) / DatasetUtil.pr(x,0,y))
        m = LogisticRegression(C=4, dual=True)
        x_nb = x.multiply(r)
        return m.fit(x_nb, y), r