import os

import pandas as pd


test = pd.read_csv('../wordsim353/combined.csv')
X_test = (test.ix[:,0:].values).astype('str')
test_corr = (test.ix[:,-1].values).astype('float32')
corr = []
t_corr=[]
os.system("javac -classpath $CLASSPATH:/media/arjunbalgovind/Data/ESA_Wiki/descartes-0.2/bin/* ESA.java")
for file in os.listdir('data'):
    os.system("java -classpath $CLASSPATH:/media/arjunbalgovind/Data/ESA_Wiki/descartes-0.2/bin/* ESA /media/arjunbalgovind/Data/ESA_Wiki/descartes-0.2/data/wiki-index/ 3000 data/"+file+" > vectors/"+file)
    os.system("sed -i 1,6d vectors/"+file)
    print file + " Completed."
    #     corr.append(cosineSim(WordRep[vocab_dict[PorterStemmer().stem(X_test[i][0])]], WordRep[vocab_dict[PorterStemmer().stem(X_test[i][1])]]))
    #     t_corr.append(test_corr[i])
    # except:
    #     pass
