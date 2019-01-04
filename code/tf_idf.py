import numpy as np 
import sys

def create_tfidf():
    tdMatrix=np.genfromtxt(str(sys.argv[1]),dtype=float,delimiter=',',skip_header=1)
    maxFreq=np.max(np.sum(tdMatrix,axis=1))
    idfMatrix=tdMatrix.copy()
    # print "Here"
    with open(str(sys.argv[1]),'r') as f:
        header=f.readline()
        # print header
    word_idf=np.zeros(tdMatrix.shape[1])
    idfMatrix[idfMatrix>0]=1
    # print idfMatrix[0]
    word_idf = np.log(tdMatrix.shape[0]/np.sum(idfMatrix, axis=0))
    # tf_idfMat = np.square(tdMatrix)
    tf_idfMat = np.multiply(np.power(tdMatrix,3),word_idf)
    # print tf_idfMat.shape
    np.savetxt(str(sys.argv[2]),tf_idfMat,fmt='%.10f',delimiter=',',header=header,comments='')
create_tfidf()