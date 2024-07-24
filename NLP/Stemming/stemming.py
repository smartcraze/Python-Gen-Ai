import nltk
from nltk.stem import PorterStemmer,SnowballStemmer,LancasterStemmer
print("----------portersteamer--------------------")
porter_stemmer = PorterStemmer()
words = ["running", "runner", "ran", "runs", "easily", "fairly"]
stemmed_words = [porter_stemmer.stem(word) for word in words]
print(stemmed_words)
## snowball steamingg
print("----------snowball--------------------")
snowball_stemmer = SnowballStemmer("english")
for i in words:
    stemword=snowball_stemmer.stem(i)
    print(stemword)


# Lancaster Stemmer
print("----------lancaster--------------------")
lanscaststeam = LancasterStemmer()
for i in words:
    stemword=lanscaststeam.stem(i)
    print(stemword)

print("----------------------------comparison--------------")

porter_stemmer = PorterStemmer()
snowball_stemmer = SnowballStemmer("english")
lancaster_stemmer = LancasterStemmer()

porter_stemmed = [porter_stemmer.stem(word) for word in words]
snowball_stemmed = [snowball_stemmer.stem(word) for word in words]
lancaster_stemmed = [lancaster_stemmer.stem(word) for word in words]

print("Original Words:", words)
print("Porter Stemmer:", porter_stemmed)
print("Snowball Stemmer:", snowball_stemmed)
print("Lancaster Stemmer:", lancaster_stemmed)


print("-----------example using the porter stem-----------")


sentence = "The runners are running easily and fairly."
words = nltk.word_tokenize(sentence)

porter_stemmed_sentence = [porter_stemmer.stem(word) for word in words]
print("Original Sentence:", sentence)
print("Porter Stemmed Sentence:", " ".join(porter_stemmed_sentence))
