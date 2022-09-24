from utility import *
from spectral import spectral_clustering
from meanshift import mean_shift
from LCA import lca

FILEPATH = "data/semeion.data"

# K_CLUSTERs = 10

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    df = np.loadtxt(FILEPATH, delimiter=None)

    df = df[np.random.choice(df.shape[0], size=1450, replace=False), :]

    features = df[:, :256]  # record and 256 features representing the handwritten digits
    digits = df[:, 256:266]  # id_record and a vector of lenght 10 with a 1 in the position of the actual digit
    actual_digits = nonzero_indeces(digits)  # actual digits for each row

    #'''
    # Spectral clustering ----------------------------------------------------------------------------------------------
    #f = open("spectral_rand_cluster.txt", "w")
    #f.write("k_cluster\trand_index\n")
    for k in range(5, 16):
        spectral_labels = spectral_clustering(features, k)

        rand_i = rand_index(spectral_labels, actual_digits)
        print("[Spectral Clustering] - With ", k, " clusters, Rand index is: ", rand_i)
        # to print clusters in greyscale digits
        models_as_grayscales(features, spectral_labels, k)
        #f.write(str(k) + "\t" + str(rand_i) + "\n")

    #f.close()
    #'''

    '''
    # Mean shift -------------------------------------------------------------------------------------------------------
    bands_array = np.zeros(31 - 18 + 1)
    kCluster_array = np.zeros(31 - 18 + 1)
    randInd_array = np.zeros(31 - 18 + 1)
    i = 0
    for b in range(31, 18, -1):
        band = b / 10
        ms_labels, n_clusters_ = mean_shift(features, band)

        randIndex = rand_index(ms_labels, actual_digits)
        print("[Mean Shift] - With ", band, " bandwidth, Rand index is: ", randIndex)
        # to print clusters in greyscale digits
        #models_as_grayscales(features, ms_labels, n_clusters_)
        bands_array[i] = band
        kCluster_array[i] = n_clusters_
        randInd_array[i] = randIndex
        i += 1

    f = open("meanshift_rand_cluster.txt", "w")
    f.write("k_cluster\trand_index\n")
    for j in range(i):
        f.write(str(kCluster_array[j]) + "\t" + str(randInd_array[j]) + "\n")
    f.close()
    '''

    '''
    #  Latent Class Analysis -------------------------------------------------------------------------------------------
    f = open("lca_rand_cluster.txt", "w")
    f.write("k_cluster\trand_index\n")
    for k in range(5, 16):
        # print("Starting LCA... ", end=" ")
        # start = time.time()
        pi, mu, lca_res = lca(features, k, n_iter=1000, delta=1e-13)
        lca_labels = nonzero_indeces(lca_res)
        # end = time.time()
        # print(end - start, " s")

        rand_i = rand_index(lca_labels, actual_digits)
        print("[LCA] - With ", k, " clusters, Rand index is: ", rand_i)
         # to print clusters in greyscale digits
        #models_as_greyscales(mu, k)
        f.write(str(k) + "\t" + str(rand_i) + "\n")

    f.close()
    '''
