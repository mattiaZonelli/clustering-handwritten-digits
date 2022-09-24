import numpy as np
from utility import *

'''
cited forumulas are taken from Chapter 9 of Bishop - Pattern recognition and Machine Learning
'''

# formula (9.44)
def bernulli(df, mu):
    n = len(df)  # rows of dataframe
    k = len(mu)  # numbers of clusters
    prob = np.zeros((n, k))
    for i in range(n):
        for j in range(k):
            prob[i, j] = np.prod((mu[j] ** df[i]) * ((1 - mu[j]) ** (1 - df[i])))
    return prob


# formula 9.56
def responsabilityB(df, mu, pi):
    numerator = bernulli(df, mu) * pi

    summation = numerator.sum(axis=1) + 1e-130
    denominator = summation.reshape(len(numerator), 1)

    return numerator / denominator


# formula 9.55
def logLikelihood(df, mu, pi):
    n = len(df)  # rows of dataframe
    k = len(mu)  # numbers of clusters
    responsability = responsabilityB(df, mu, pi)  # E step
    logLike = 0  # expected log likelihood
    for i in range(n):
        sumK = 0
        for j in range(k):
            '''
            x_n*ln(mu_k) + (1-x_n)*ln(1-mu_k)
            regola del esponente ->
            ln(mu_k ^ x_n) + ln( (1-mu_k)^(1-x_n) )
            logaritmo del prodotto ->
            ln[ (mu_k ^ x_n) * ( (1-mu_k)^(1-x_n) ) ]
            '''
            temp = ((mu[j] ** df[i]) * ((1 - mu[j]) ** (1 - df[i])))
            sumK += responsability[i, j] * (np.log(pi[j]) + np.sum(np.log(temp.clip(min=1e-50))))
        logLike += sumK

    return logLike, responsability


# M(maximization) step
def Mstep(df, responsability):
    n = len(df)  # rows of dataframe
    k = len(responsability[0])  # numbers of clusters
    d = len(df[0])
    nk = np.sum(responsability, axis=0)  # 9.57
    mu = np.empty((k, d))

    # compute mu as matrix
    for i in range(k):
        gamma = (responsability[:, i]).reshape(len(df), 1)
        mu[i] = np.sum(gamma * df, axis=0) / (nk[i] + 1e-130)  # 9.58

    return nk / n, mu  # 9.60, 9.59


def EMalg(df, pi, mu, n_iter, delta):
    # compute loglikelihood
    loglike, responsability = logLikelihood(df, mu, pi)
    loglike_prev = loglike
    for i in range(n_iter):
        pi, mu = Mstep(df, responsability)
        # re-compute the estimation of log likelihood with the updated parameters
        loglike, responsability = logLikelihood(df, mu, pi)
        # check for convergence
        if np.abs(loglike - loglike_prev) < delta:
            break
        else:
            loglike_prev = loglike

    return pi, mu, responsability


def lca(df, k, n_iter=10000, delta=1e-20):
    pi = np.random.uniform(0.25, 0.75, k)
    tot = np.sum(pi)
    mu = np.full((k, len(df[0])), 1.0 / k)
    return EMalg(df, pi / tot, mu, n_iter, delta)
