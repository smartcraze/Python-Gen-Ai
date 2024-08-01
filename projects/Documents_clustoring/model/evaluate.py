# evaluate.py
import pandas as pd
from sklearn.metrics import silhouette_score, davies_bouldin_score

def evaluate_clusters(data, cluster_labels):
    silhouette = silhouette_score(data, cluster_labels)
    davies_bouldin = davies_bouldin_score(data, cluster_labels)
    return silhouette, davies_bouldin

if __name__ == "__main__":
    data = pd.read_csv('../data/features.csv')
    clusters = pd.read_csv('../data/clustered_documents.csv')

    kmeans_labels = clusters['KMeans_Cluster']
    hierarchical_labels = clusters['Hierarchical_Cluster']
    
    kmeans_silhouette, kmeans_davies_bouldin = evaluate_clusters(data, kmeans_labels)
    hierarchical_silhouette, hierarchical_davies_bouldin = evaluate_clusters(data, hierarchical_labels)
    
    print(f"KMeans - Silhouette Score: {kmeans_silhouette}, Davies-Bouldin Index: {kmeans_davies_bouldin}")
    print(f"Hierarchical - Silhouette Score: {hierarchical_silhouette}, Davies-Bouldin Index: {hierarchical_davies_bouldin}")
