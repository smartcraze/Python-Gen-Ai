import nltk
from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
import string

from gensim.models import word2vec
import numpy as np


## Pre-process the data 

nltk.download('punkt')
nltk.download('stopwords')

def Preprocess(text):
    # Tokenise word 
    tokens = word_tokenize(text.lower())

    # cleaning
    tokens = [word for word in tokens if word.isalnum() and word not in stopwords.words('english') ]

    return tokens
    

documents = [
    "Machine learning is fascinating.",
    "Artificial intelligence is a broad field.",
    "Data science involves statistics.",
    "Deep learning is a part of machine learning.",
    "Natural language processing is a key AI component."
]


# Preprocess documents
tokenized_documents = [Preprocess(doc) for doc in documents]

print(tokenized_documents)

##  training the model 

model = Word2Vec(tokenized_documents, vector_size=100, window=5, min_count=1, workers=4)





def get_average_vector(tokens, model):
    vectors = [model.wv[word] for word in tokens if word in model.wv]
    return np.mean(vectors, axis=0) if vectors else np.zeros(model.vector_size)

document_vectors = [get_average_vector(doc, model) for doc in tokenized_documents]












# if __name__ =="__main__":
#     pass


