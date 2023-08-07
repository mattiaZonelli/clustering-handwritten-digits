# Unsupervised learnig: Clustering on handwritten digits

The goal of the assignment was to perform classification over the Semeion Handwritten Digit data set using:
- Latent Class Analysis (LCA);
- Mean Shift;
- Normalized cut.
for the mean shift and normalized cut, we assume that the images are vectors in a 256-dimensional Euclidean space.
The number of clusters k varies from 5 to 15, for LCA and normalized-cut, while for mean shift vary the kernel width.


LCA models can be referred to as finite mixtures of Bernoulli distributions so we coded the EM algorithm supposing that 
given a Bernoulli mixture model, the goal is to maximize the likelihood function with respect to the parameters.
Because it is not guaranteed that the Mean shift will converge in a high dimensional space like in our case, 
we need to apply Principal Component Analysis (PCA) to our dataset before actually running the mean shift algorithm.
For both PCA and Mean shift, we used the functions present in scikit-learn.
Also for the spectral clustering algorithm we used the function provided by sklearn.

The three models are compared by rand index and by plotting each computed cluster in grey scale.

You can find more in the "report.pdf" file!
