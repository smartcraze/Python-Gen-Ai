from gensim.models import Word2Vec

# Example larger corpus
sentences = [
    ['i', 'love', 'machine', 'learning'],
    ['deep', 'learning', 'is', 'a', 'subset', 'of', 'machine', 'learning'],
    ['natural', 'language', 'processing', 'is', 'a', 'part', 'of', 'ai'],
    ['hello', 'world'],
    ['hello', 'suraj'],
    ['world', 'is', 'big'],
    ['big', 'world', 'suraj'],
    ['artificial', 'intelligence', 'is', 'the', 'future'],
    ['machine', 'learning', 'is', 'fun'],
    ['deep', 'learning', 'models', 'require', 'a', 'lot', 'of', 'data'],
    ['nlp', 'stands', 'for', 'natural', 'language', 'processing']
]

# Train the Word2Vec model
model = Word2Vec(sentences, vector_size=50, window=5, min_count=1, workers=4)

# Get the vector for the word 'machine'
vector_machine = model.wv['machine']
print("Vector for 'machine':", vector_machine)

# Find the top 5 words similar to 'machine'
similar_words_machine = model.wv.most_similar('machine', topn=5)
print("Words similar to 'machine':", similar_words_machine)

# Find the top 5 words similar to 'learning'
similar_words_learning = model.wv.most_similar('learning', topn=5)
print("Words similar to 'learning':", similar_words_learning)

# Find the word that doesn't match in the list
odd_one_out = model.wv.doesnt_match(['machine', 'learning', 'deep', 'elephant'])
print("The word that doesn't",odd_one_out)
