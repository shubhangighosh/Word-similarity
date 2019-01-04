# import modules 
import gensim, logging
from nltk.corpus import brown
import textmining
from nltk.tokenize import RegexpTokenizer
import re
from string import digits
from nltk.corpus import stopwords
import enchant
from nltk.stem.porter import *
from nltk.tokenize import sent_tokenize
import pandas as pd
from scipy.stats import spearmanr
import numpy as np
import csv
#set up logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)



#UK English Dictionary
d = enchant.Dict("en_UK")
tokenizer = RegexpTokenizer(r'\w+')
sentences = []

sent_tokenize_list = sent_tokenize(brown.raw())
for s in sent_tokenize_list:
	text = tokenizer.tokenize(s.encode('ascii','ignore').translate(None, digits).lower())
	filtered_sent = ''
	for w in text:
		#checking for non-words
	    if d.check(w) == True:
	        filtered_sent += PorterStemmer().stem(w)
	        filtered_sent += ' '
	sentences.append(filtered_sent.split())



#csv file to write similarity scores to
file = open('word2vec.csv','w')
writer = csv.writer(file,  lineterminator='\n')
#Word2vec model
model = gensim.models.Word2Vec(sentences,min_count = 2, sg = 1, hs = 1, size = 2000)
#Wordsim-353 dataset
test = pd.read_csv('wordsim353/combined.csv')
X_test = (test.ix[:,0:].values).astype('str')
#test scores -- Wordsim-353
test_corr = (test.ix[:,-1].values).astype('float32')
#Word2vec scores
corr = []
#iterating over Wordsim-353 dataset
for i in range(len(X_test)):
	#stemming
	stem1 = PorterStemmer().stem(X_test[i][0])
	stem2 = PorterStemmer().stem(X_test[i][1])
	if (stem1 in model.wv.vocab) and (stem2 in model.wv.vocab):
		corr.append(model.similarity(stem1, stem2))
	else:
		corr.append(0.5) #for words not in vocab
	
	#writing to csv
	writer.writerow([X_test[i][0] , X_test[i][1], corr[i], test_corr[i], '\n'])
	

	

file.close()

corr = np.array(corr)
#spearman correlation
print spearmanr(test_corr/10.0, corr)[0]


#Google pre-trained vectors
model = gensim.models.KeyedVectors.load_word2vec_format('./model/GoogleNews-vectors-negative300.bin', binary=True)
corr_google = []
for i in range(len(X_test)):
	#stemming
	stem1 = PorterStemmer().stem(X_test[i][0])
	stem2 = PorterStemmer().stem(X_test[i][1])
	if (stem1 in model.wv.vocab) and (stem2 in model.wv.vocab):
		corr_google.append(model.similarity(stem1, stem2))
	else:
		corr_google.append(0.5)
corr_google = np.array(corr_google)
print spearmanr(test_corr/10.0, corr_google)[0]
