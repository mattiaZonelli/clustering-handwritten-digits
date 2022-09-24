import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, normalize
from sklearn.decomposition import PCA
from itertools import islice, cycle


def models_as_grayscales(features, labels, n_cluster):
    models = np.zeros(shape=(n_cluster, 256))
    #counter = np.zeros(n_cluster)
    for i in range(labels.shape[0]):
        models[labels[i]] += features[i]
        #counter[labels[i]] += 1

    #models = models / counter.reshape((n_cluster, 1))

    fig, axs = plt.subplots(nrows=1, ncols=n_cluster, figsize=(n_cluster*3, 8))
    for i in range(n_cluster):
        axs[i].set_title("Cluster " + str(i))
        box = models[i].reshape((16, 16))
        axs[i].imshow(box, cmap='gray_r')
    plt.show()

# og version for LCA
def models_as_greyscales(models, n_cluster):
    fig, axs = plt.subplots(nrows=1, ncols=n_cluster, figsize=(n_cluster * 3, 8))
    for i in range(n_cluster):
        axs[i].set_title("Cluster " + str(i))
        box = models[i].reshape((16, 16))
        axs[i].imshow(box, cmap='gray_r')
    plt.show()


# function to compute the Rand index from the labels retrived by a clustering algorithm and the actual digits
def rand_index(cluster_labels, actual_digits):
    n = len(actual_digits)
    # Nested loop for all possible pairs
    a = 0
    b = 0
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            # increase a when all is the same
            if actual_digits[i] == actual_digits[j] and cluster_labels[i] == cluster_labels[j]:
                a += 1
            # increase a when all is the different
            if actual_digits[i] != actual_digits[j] and cluster_labels[i] != cluster_labels[j]:
                b += 1
    # directly return the rand index
    return 2 * (a + b) / (n * (n - 1))

# to retrix indexes of non zero elements in an array
def nonzero_indeces(classes):
    ris = np.empty(len(classes), dtype='int')
    for i in range(0, classes.shape[0]):
        ris[i] = np.nonzero(classes[i])[0][0]
    return ris

# to show how clustered data appears in a linear space
def colored_plot(df, labels, k_clusters, alg_name):
    if k_clusters <= 15:
        colors = np.array(list(islice(cycle(['black', 'indigo', 'red', 'darkkhaki', 'darkorange',
                                             'gold', 'green', 'lime', 'aquamarine', 'blue',
                                             'grey', 'mediumorchid', 'hotpink', 'steelblue', 'darkred'
                                             ]),
                                      int(max(labels) + 1))))
        # add black color for outliers (if any)
        colors = np.append(colors, ["#000000"])
        plt.figure(figsize=(8, 8))
        plt.scatter(df['P0'], df['P1'], color=colors[labels])
        plt.xticks()
        plt.yticks()
        plt.title(alg_name + ' with ' + str(k_clusters) + ' clusters')
        plt.show()


'''
# to visualize a single cluster/image
def print_as_number(line):
    box = np.reshape(line, (-1, 16))
    # print(box)
    plt.imshow(box, cmap='gray_r')
    plt.show()
'''