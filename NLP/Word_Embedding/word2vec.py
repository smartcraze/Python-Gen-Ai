from gensim.models import Word2Vec
## corpus

sentences = [
    ['hello', 'world'],
    ['hello', 'suraj'],
    ['world', 'is', 'big'],
    ['big', 'world', 'suraj']
]
## Training the Word2Vec model

model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)


##Get the vector for a word
vector = model.wv['hello']

print("Vector for 'hello':", vector)


# Finding similar words
similar_words = model.wv.most_similar('hello', topn=5)
print("Words similar to 'hello':", similar_words)
