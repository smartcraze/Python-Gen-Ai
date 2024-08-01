# clustering.py
import pandas as pd
from sklearn.cluster import KMeans, AgglomerativeClustering

def kmeans_clustering(data, num_clusters):
    kmeans = KMeans(n_clusters=num_clusters)
    clusters = kmeans.fit_predict(data)
    return clusters

def hierarchical_clustering(data, num_clusters):
    hierarchical = AgglomerativeClustering(n_clusters=num_clusters)
    clusters = hierarchical.fit_predict(data)
    return clusters

if __name__ == "__main__":
    data = pd.read_csv('../features.csv')
    num_clusters = 5  # You can change the number of clusters

    kmeans_clusters = kmeans_clustering(data, num_clusters)
    hierarchical_clusters = hierarchical_clustering(data, num_clusters)
    
    # Save the clusters to a file
    data['KMeans_Cluster'] = kmeans_clusters
    data['Hierarchical_Cluster'] = hierarchical_clusters
    data.to_csv('../data/clustered_documents.csv', index=False)
