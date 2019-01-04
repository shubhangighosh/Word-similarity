# Word-similarity
Four word similarity methods are trained on three corpora. Their properties are evaluated through experiments. 
Methods:  
1. Explicit Semantic Analysis  
2. Latent Semantic Analysis  
3. Wordnet-based similarity  
4. Word2vec  
  
Corpora:
1. Brown corpus  
2. 20NewsGroup  
3. Reuters  
  
Dependencies:
1. Enchant: pip install pyenchant
2. Brown Corpus: import nltk, nltk.download('brown')
3. Stopwords: import nltk, nltk.download('stopwords') on python console
4. Download google pretrained word2vec model from : https://drive.google.com/file/d/0B7XkCwpI5KDYNlNUTTlSS21pQmM/edit and save in folder 'model' inside the main repository folder.



Execution Procedure:
1. TD Matrix and Term Weighting Matrix: First run tdm.py to obtain a term document matrix. Then run tf_idf.py "TD Matrix filename" "New weighted matrix", to obtain the weighted matrix to be used in LSA.
2. ESA: First the Wikipedia dump needs to be downloaded, and using Descartes the inverted index file has to be created. The the following scripts need to be executed in order:
    a. create_inputs.py
    b. esa_createVec.py
    c. esa_evalVec.py
3. LSA: Run lsa.py create "Weight matrix" u.csv s.csv. After this run lsa.py "Concept count" u.csv s.csv lsa_vectors.csv.
4. Word2Vec: Run 'python word2vec.py' in console.
5. Wordnet: Run 'python wordnet.py' in console.
