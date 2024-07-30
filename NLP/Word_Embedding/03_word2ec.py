from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize, sent_tokenize

# Define the corpus
corpus = "Hey this is suraj vishwakarma trying to perform the word to vec algorithm through tokenisation and i am trying to put in the machine learning algo"

# Tokenize the corpus into sentences and then into words
sentences = sent_tokenize(corpus)
tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]

print(tokenized_sentences)

# Train the model
model = Word2Vec(tokenized_sentences, vector_size=100, window=5, min_count=1, workers=4)

# Get the vector for the word 'machine'
vector_machine = model.wv['machine']
print('Vector for the word "machine":')
print(vector_machine)
