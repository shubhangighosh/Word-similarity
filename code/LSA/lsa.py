import numpy as np 
import sys
import pandas as pd
from scipy.stats import spearmanr,pearsonr
from nltk.stem.porter import *
# arg 1: create, or number of dimensions
# arg 2: tf_idf mat
# arg 3,4: U and S file
# arg 5 to store word reps

def perform_svd():
    input_file=str(sys.argv[2])
    tf_idfMatrix=np.genfromtxt(input_file,dtype=float,delimiter=',',skip_header=1)
    U, S, VT = np.linalg.svd(np.transpose(tf_idfMatrix),full_matrices=False)
    # print U,shape, S.shape, VT.shape
    np.savetxt(str(sys.argv[3]),U,fmt='%.20f',delimiter=',',comments='')
    np.savetxt(str(sys.argv[4]),S,fmt='%.20f',delimiter=',',comments='')
    # np.savetxt(str(sys.argv[5]),VT,fmt='%.2f',delimiter=',',comments='')

def cosineSim(a,b):
    # print np.dot(a,b), (np.linalg.norm(a) * np.linalg.norm(b))
    return np.dot(a,b)/(np.linalg.norm(a) * np.linalg.norm(b))

def genWordReps(dim_count):
    U=np.genfromtxt(str(sys.argv[2]),dtype=float,delimiter=',',skip_header=0)
    S=np.genfromtxt(str(sys.argv[3]),dtype=float,delimiter=',',skip_header=0)
    # VT=np.genfromtxt(str(sys.argv[3]),dtype=float,delimiter=',',skip_header=0)
    WordRep=np.dot(U[:,:dim_count],np.diag(S[:dim_count]))
    # print WordRep.shape, U.shape, S.shape
    np.savetxt(str(sys.argv[4]),WordRep,fmt='%.2f',delimiter=',',comments='')
    with open('Vocab.txt','r') as f:
        vocab_header=f.readline()
    vocab_header=vocab_header.split(',')
    vocab_dict = dict((word,index) for index,word in enumerate(vocab_header))
    test = pd.read_csv('../wordsim353/combined.csv')
    X_test = (test.ix[:,0:].values).astype('str')
    test_corr = (test.ix[:,-1].values).astype('float32')
    corr = []
    t_corr=[]
    for i in range(len(X_test)):
        try:
            cs=cosineSim(WordRep[vocab_dict[PorterStemmer().stem(X_test[i][0])]], WordRep[vocab_dict[PorterStemmer().stem(X_test[i][1])]])
            corr.append(cs)
            t_corr.append(test_corr[i])
            # print X_test[i][0], X_test[i][1], cs, test_corr[i]
        except:
            pass
        # try:
        #     print X_test[i][0], X_test[i][1], cosineSim(WordRep[vocab_dict[PorterStemmer().stem(X_test[i][0])]], WordRep[vocab_dict[PorterStemmer().stem(X_test[i][1])]]), test_corr[i]
        # except:
        #     print  0, test_corr[i]
        # corr.append(model.similarity(X_test[i][0], X_test[i][1]))
       
    # print(len(corr),len(t_corr))

    corr = np.nan_to_num(np.array(corr))
    print spearmanr(corr, t_corr)



if str(sys.argv[1])=='create':
    perform_svd()
elif str(sys.argv[1])=='all':
    for i in range(5,500,5):
        print(i)
        genWordReps(i)

else:
    genWordReps(int(sys.argv[1]))

