#!/usr/bin/env python
# coding: utf-8

# # Final Year Project - B15
# 
# 

# In[1]:


import sys, os, re, csv, codecs, numpy as np, pandas as pd
import tensorflow

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import Dense, Input, LSTM, Embedding, Dropout, Activation
from tensorflow.keras.layers import Bidirectional, GlobalMaxPool1D
from tensorflow.keras.models import Model
from tensorflow.keras import initializers, regularizers, constraints, optimizers, layers
from tensorflow.keras.models import load_model

from tensorflow.keras import backend as K
# We include the GloVe word vectors in our input files. To include these in your kernel, simple click 'input files' at the top of the notebook, and search 'glove' in the 'datasets' section.

# In[2]:


path = '/'
#EMBEDDING_FILE='glove.6B.50d.txt'
TRAIN_DATA_FILE='train.csv'
TEST_DATA_FILE='test.csv'


# Set some basic config parameters:

# In[3]:


embed_size = 50 # how big is each word vector
max_features = 20000 # how many unique words to use (i.e num rows in embedding vector)
maxlen = 100 # max number of words in a comment to use


# Read in our data and replace missing values:

# In[4]:


train = pd.read_csv(TRAIN_DATA_FILE)
test = pd.read_csv(TEST_DATA_FILE)

list_sentences_train = train["comment_text"].fillna("_na_").values
list_classes = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]
y = train[list_classes].values
list_sentences_test = test["comment_text"].fillna("_na_").values


# In[40]:




#list_sentences_test[0]="i love this country."
#print(list_sentences_test[0])


# In[6]:


tokenizer = Tokenizer(num_words=max_features)
print(tokenizer)


# In[ ]:


tokenizer.fit_on_texts(list(list_sentences_train))


# In[41]:

def  messagechecker(messageinput):
			K.clear_session()




			list_sentences_test[0]=messageinput
			print(list_sentences_test[0])

			list_tokenized_test = tokenizer.texts_to_sequences((list_sentences_test))

			X_te = pad_sequences(list_tokenized_test, maxlen=maxlen)


			# In[51]:


			print(X_te)

			X_te=X_te[:1]


			# In[52]:


			print([X_te])


			# In[32]:


			model = load_model('trained.h5')


			# In[53]:


			y_test = model.predict([X_te], batch_size=1024, verbose=1)


			# In[54]:


			print(y_test)


			# In[46]:


			#act_pred = pd.read_csv('sample_submission.csv')
			#act_pred[list_classes] = y_test
			#act_pred.to_csv('predictedAttr.csv', index=False)


			# In[55]:


			y_test[y_test >= 0.5] = 1
			y_test[y_test < 0.5] = 0
			y_test


			# In[56]:


			#bin_pred = pd.read_csv('sample_submission.csv')
			#bin_pred[list_classes] = y_test
			#bin_pred.to_csv('predictions.csv', index=False)


			# In[57]:


			y_test


			# In[ ]:


			print("the final results are",y_test)

			total_result=y_test[0][0] + y_test[0][1] + y_test[0][2] + y_test[0][3] + y_test[0][4] + y_test[0][5]

			print(total_result)

			if  total_result==0:
				print("possitive")
				return messageinput

			else:

				print("negative")
				b="***********"
				return b
			K.clear_session()


			


			# In[ ]:




