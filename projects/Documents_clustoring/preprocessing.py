
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
import string

nltk.download('punkt')
nltk.download('stopwords')

def preprocess(text):
    # Tokenization
    tokens = word_tokenize(text)
    
    # Convert to lower case
    tokens = [word.lower() for word in tokens]
    
    # Remove punctuation
    table = str.maketrans('', '', string.punctuation)
    tokens = [word.translate(table) for word in tokens]
    
    # Remove non-alphabetic tokens
    tokens = [word for word in tokens if word.isalpha()]
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if not word in stop_words]
    
    # Stemming
    porter = PorterStemmer()
    tokens = [porter.stem(word) for word in tokens]
    
    return tokens

def preprocess_documents(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            tokens = preprocess(line)
            outfile.write(' '.join(tokens) + '\n')

if __name__ == "__main__":
    preprocess_documents('../data/raw_documents.txt', '../data/processed_documents.txt')
