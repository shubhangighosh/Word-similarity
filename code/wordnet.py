#importing modules
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
from scipy.stats import spearmanr
import pandas as pd
import numpy as np
import csv

#semcor for information content based measures
semcor_ic = wordnet_ic.ic('ic-semcor.dat')
#wordsim353
test = pd.read_csv('wordsim353/combined.csv')
X_test = (test.ix[:,0:].values).astype('str')
test_score = (test.ix[:,-1].values).astype('float32')
score_lch = []
score_wup = []
score_jcn = []

#writing similarity scores to csv
file = open('wordnet.csv','w')
writer = csv.writer(file,  lineterminator='\n')

for i in range(len(X_test)):
	temp_score_lch = 0
	temp_score_wup = 0
	
	temp_score_jcn = 0
	#iterating over synsets
	for syn1 in wn.synsets(X_test[i][0]):
		for syn2 in wn.synsets(X_test[i][1]):
			
			if syn1.pos() == syn2.pos():
				#path based -- lch
				if wn.lch_similarity(syn1,syn2)!= None:
					#max synset similarity used
					temp_score_lch = max(wn.lch_similarity(syn1,syn2),temp_score_lch)
				#Information content based similarity --jcn
				#ommiting words which have no part of speech tag in ic
				try:
					if wn.jcn_similarity(syn1,syn2, semcor_ic)!= None:
						temp_score_jcn = max(wn.jcn_similarity(syn1,syn2, brown_ic),temp_score_jcn)
				except:
					print(" ")
				
			#path based --wup
			if wn.wup_similarity(syn1,syn2)!= None:
				temp_score_wup = max(wn.wup_similarity(syn1,syn2),temp_score_wup)
				
	
	
	score_lch.append(temp_score_lch)
	score_wup.append(temp_score_wup)
	score_jcn.append(temp_score_jcn)
	#writing to csv
	writer.writerow([X_test[i][0] , X_test[i][1], temp_score_lch, temp_score_wup, temp_score_jcn, test_score[i], '\n'])	
	
file.close()
score_lch = np.array(score_lch)
score_wup = np.array(score_wup)
score_jcn = np.array(score_jcn)

print "Leacock-Chodorow Similarity:", spearmanr(score_lch, test_score/10.0)[0]
print "Wu-Palmer Similarity:", spearmanr(score_wup, test_score/10.0)[0]
print "Jiang-Conrath Similarity:", spearmanr(score_jcn, test_score/10.0)[0]
