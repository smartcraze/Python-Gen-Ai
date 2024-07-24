### Wordnet Lemmatizer

from nltk.stem import WordNetLemmatizer

Lemmatizer =  WordNetLemmatizer()
'''
pos =
noun -n
verb -v
adjective -a
adverb -r

'''
going = Lemmatizer.lemmatize('going',pos='v')

print(going)

words = ["running",'goes','supportingly', "runner","history", "ran", "runs", "easily", "fairly"]
for word in words:
    print(word + "--->"+Lemmatizer.lemmatize(word,pos='r'))

