
import subprocess

if __name__ == "__main__":
    # Run preprocessing
    subprocess.run(['python', 'preprocessing/preprocess.py'])
    
    # Run feature extraction
    subprocess.run(['python', 'feature_extraction/extract_features.py'])
    
    # Run clustering
    subprocess.run(['python', 'model/clustering.py'])
    
    # Run evaluation
    subprocess.run(['python', 'model/evaluate.py'])
    
    # Run visualization
    subprocess.run(['python', 'visualization/visualize.py'])
