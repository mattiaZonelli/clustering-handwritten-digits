from sklearn.cluster import MeanShift
from utility import *


def mean_shift(features, bandwidth):

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(features)

    '''
    # Variance changes
    # Reducing the dimensions of the data
    pca = PCA(n_components=20)  # the lower the number of components, the lower will be the precision
    principalComponents = pca.fit_transform(X_scaled)
    # Plot the explained variances
    features = range(1, pca.n_components_)
    plt.bar(features, pca.explained_variance_ratio_[1:,], color='black')
    plt.xlabel('PCA features')
    plt.ylabel('variance %')
    plt.xticks(features)
    plt.show()
    '''

    pca = PCA(n_components=2)  # the lower the number of components, the lower will be the precision
    X_principal = pca.fit_transform(X_scaled)
    X_principal = pd.DataFrame(X_principal)
    # rename the columns
    X_principal.columns = ['P0', 'P1']

    # create instance of meanshift alg with the given kernel width
    ms = MeanShift(bandwidth=bandwidth)
    # fit the data
    ms.fit(X_principal)
    # get the labels
    labels = ms.labels_
    # cluster_centers = ms.cluster_centers_

    # find the unique labels
    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)

    # show cluster in different colors
    colored_plot(X_principal, labels, n_clusters_, "Mean shift")

    print("number of estimated clusters : %d" % n_clusters_)

    return labels, n_clusters_



