from nltk.tokenize import sent_tokenize,word_tokenize,wordpunct_tokenize
corpus = "Hey i am learning,. natural language processing!!. i am learning tokenisation guys "
token=sent_tokenize(corpus)
# print(token)
word_token= word_tokenize(corpus)
punkt_token = wordpunct_tokenize(corpus)
'''for word in word_token:
    print(word)
print(punkt_token)
'''
## steming and its types - text preprocessing



import nltk
from nltk.stem import PorterStemmer,RegexpStemmer
porter = PorterStemmer()

words = ["running", "runner", "ran", "easily", "fairly"]
stemmed_words = [porter.stem(word) for word in words]
print(stemmed_words)

st = RegexpStemmer('ing$|s$|e$|able$', min=4)

print(st.stem("eating"))



# regular expression tokenisation 
from nltk.tokenize import RegexpTokenizer

text = "Hello, world! This is a tokenization example. Let's see how it works."

# Tokenizer that matches words
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(text)
print(tokens)

# TweetTokenizer

from nltk.tokenize import TweetTokenizer

text = "Hello @world! This is a #tokenization example :)"
tweet_tokenizer = TweetTokenizer()
tokens = tweet_tokenizer.tokenize(text)
print(tokens)



## using the custome function 
import re

def custom_tokenize(text):
    # Example: Split by spaces and keep punctuation attached to words
    tokens = re.findall(r'\w+|[^\w\s]', text, re.UNICODE)
    return tokens

text = "Hello, world! This is a tokenization example."
tokens = custom_tokenize(text)
print(tokens)





text = """Hello, world! This is a tokenization example. It shows how to split sentences and words.
Let's try another sentence."""

# Tokenize into sentences
sentences = sent_tokenize(text)

# Tokenize each sentence into words
tokenized_sentences = [word_tokenize(sentence) for sentence in sentences]

print(tokenized_sentences)
