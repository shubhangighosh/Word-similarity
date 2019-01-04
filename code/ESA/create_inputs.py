import os

import pandas as pd


test = pd.read_csv('../wordsim353/combined.csv')
X_test = (test.ix[:,0:].values).astype('str')
test_corr = (test.ix[:,-1].values).astype('float32')
corr = []
t_corr=[]
for i in range(len(X_test)):
    with open("data/"+X_test[i][0]+'.txt','w') as f:
        f.write(X_test[i][0])
    with open("data/"+X_test[i][1]+'.txt','w') as f:
        f.write(X_test[i][1])

    #     corr.append(cosineSim(WordRep[vocab_dict[PorterStemmer().stem(X_test[i][0])]], WordRep[vocab_dict[PorterStemmer().stem(X_test[i][1])]]))
    #     t_corr.append(test_corr[i])
    # except:
    #     pass
