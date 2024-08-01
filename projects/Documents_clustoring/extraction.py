# extract_features.py
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def extract_features(input_file, output_file):
    with open(input_file, 'r') as file:
        documents = file.readlines()
    
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(documents)
    
    # Save the features to a CSV file
    df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    extract_features('../data/processed_documents.txt', '../data/features.csv')
