import os
import pandas as pd
import numpy as np 
from scipy.stats import spearmanr,pearsonr


def cosineSim(a,b):
    denom = (np.linalg.norm(np.array(a[1])) * np.linalg.norm(np.array(b[1])))
    numerator=0
    for i in range(len(a[0])):
        if a[0][i] in b[0]:
            numerator+=(float(a[1][i])*float(b[1][(b[0].index(a[0][i]))]))
    return numerator/denom

test = pd.read_csv('../wordsim353/combined.csv')
X_test = (test.ix[:,0:].values).astype('str')
test_corr = (test.ix[:,-1].values).astype('float32')
corr = []
t_corr=[]
for i in range(len(X_test)):
    with open("vectors/"+X_test[i][0]+'.txt','r') as f:
        a = f.readlines()
        a[0]=a[0].split('|')[:-1]
        a[1]=a[1].split('|')[:-1]
    with open("vectors/"+X_test[i][1]+'.txt','r') as f:
        b = f.readlines()
        b[0]=b[0].split('|')[:-1]
        b[1]=b[1].split('|')[:-1]

    corr.append(cosineSim(a, b))
    t_corr.append(test_corr[i])
    print X_test[i][0]+","+X_test[i][1]+":"+str(corr[i])+" "+str(t_corr[i])
    # except:
    #     pass

corr = np.nan_to_num(np.array(corr))
print spearmanr(corr, t_corr)