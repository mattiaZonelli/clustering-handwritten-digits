from sklearn.cluster import SpectralClustering
from utility import *


def spectral_clustering(features, k_clusters):
    # Preprocessing the data to make it visualizable
    # Scaling the Data
    #'''
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(features)
    # Normalizing the Data
    X_normalized = normalize(X_scaled)
    # Converting the numpy array into a pandas DataFrame
    X_normalized = pd.DataFrame(X_normalized)
    # Reducing the dimensions of the data
    pca = PCA(n_components=2)
    X_principal = pca.fit_transform(X_normalized)
    X_principal = pd.DataFrame(X_principal)
    X_principal.columns = ['P0', 'P1']
    # print(X_principal.head())

    # building spectral clustering model
    spectral_model_nn = SpectralClustering(n_clusters=k_clusters, affinity='nearest_neighbors', assign_labels='kmeans')

    # training the model and Storing the predicted cluster labels
    labels = spectral_model_nn.fit_predict(X_principal)

    # show cluster in different colors in a linear space
    colored_plot(X_principal, labels, k_clusters, "Spectral Clustering")
    #'''

    '''
    # this implementation give us better result but it does not allow to use colored_plot
    X = features

    spectral_clusters = SpectralClustering(n_clusters=k_clusters, assign_labels='kmeans', random_state=0,
                                           affinity='nearest_neighbors', eigen_solver='amg')
    labels = spectral_clusters.fit_predict(X)
    '''

    return labels
