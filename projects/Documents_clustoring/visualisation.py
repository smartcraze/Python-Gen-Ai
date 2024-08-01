# visualize.py
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import plotly.express as px

def visualize_clusters(data, cluster_labels, method='PCA'):
    if method == 'PCA':
        reducer = PCA(n_components=2)
    elif method == 'TSNE':
        reducer = TSNE(n_components=2, random_state=42)
    
    reduced_data = reducer.fit_transform(data)
    df = pd.DataFrame(reduced_data, columns=['Component 1', 'Component 2'])
    df['Cluster'] = cluster_labels

    fig = px.scatter(df, x='Component 1', y='Component 2', color='Cluster', title=f'Clusters visualized using {method}')
    fig.show()

if __name__ == "__main__":
    data = pd.read_csv('../data/features.csv')
    clusters = pd.read_csv('../data/clustered_documents.csv')

    kmeans_labels = clusters['KMeans_Cluster']
    hierarchical_labels = clusters['Hierarchical_Cluster']
    
    # Visualize KMeans clusters
    visualize_clusters(data, kmeans_labels, method='PCA')
    visualize_clusters(data, kmeans_labels, method='TSNE')
    
    # Visualize Hierarchical clusters
    visualize_clusters(data, hierarchical_labels, method='PCA')
    visualize_clusters(data, hierarchical_labels, method='TSNE')
