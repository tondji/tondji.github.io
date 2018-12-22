
# coding: utf-8

# In[29]:

import numpy as np
from scipy.stats import multivariate_normal as mvn

class GaussianMixtureModel():
    """Density estimation with Gaussian Mixture Models (GMM).

    You can add new functions if you find it useful, but **do not** change
    the names or argument lists of the functions provided.
    """
    def __init__(self, X, K):
        """Initialise GMM class.

        Arguments:
          X -- data, N x D array
          K -- number of mixture components, int
        """
        self.X = X
        self.n = X.shape[0]
        self.D = X.shape[1]
        self.K = K


    def E_step(self, mu, S, pi):
        """Compute the E step of the EM algorithm.

        Arguments:
          mu -- component means, K x D array
          S -- component covariances, K x D x D array
          pi -- component weights, K x 1 array

        Returns:
          r_new -- updated component responsabilities, N x K array
        """
        # Assert that all arguments have the right shape
        assert(mu.shape == (self.K, self.D) and               S.shape  == (self.K, self.D, self.D) and               pi.shape == (self.K, 1))
        r_new = np.zeros((self.n, self.K))

        # Task 1: implement the E step and return updated responsabilities
        # Write your code from here...

        for i in range(self.n): 
            Nk = 0
            for j in range(self.K):
                Nk += pi[j] * mvn.pdf((self.X)[i], mu[j], S[j], allow_singular=True)
            for k in range(self.K):
                r_new[i, k] = pi[k] * mvn.pdf((self.X)[i], mu[k], S[k], allow_singular=True)/ Nk
        
        # ... to here.
        assert(r_new.shape == (self.n, self.K))
        return r_new


    def M_step(self, mu, r):
        """Compute the M step of the EM algorithm.

        Arguments:
          mu -- previous component means, K x D array
          r -- previous component responsabilities,  N x K array

        Returns:
          mu_new -- updated component means, K x D array
          S_new -- updated component covariances, K x D x D array
          pi_new -- updated component weights, K x 1 array
        """
        assert(mu.shape == (self.K, self.D) and               r.shape  == (self.n, self.K))
        mu_new = np.zeros((self.K, self.D))
        S_new  = np.zeros((self.K, self.D, self.D))
        pi_new = np.zeros((self.K, 1))

        # Task 2: implement the M step and return updated mixture parameters
        # Write your code from here...

        #updating mu and pi
        for k in range(self.K):
            Nk = 0
            for j in range(self.n):
                Nk += r[j,k]
            for i in range(self.n):
                mu_new[k] += (r[i, k] * (self.X)[i])
            mu_new[k] /= Nk
            pi_new[k] = Nk/ (self.n)
        
        #updating S
        for k in range(self.K):
            Nk = 0
            for i in range(self.n): 
                Nk += r[i,k]
            for i in range(self.n):
                ys = np.reshape((self.X)[i]- mu_new[k], (-1,1))
                S_new[k] += (r[i, k] * (ys @ (ys.T)))
            S_new[k] /= Nk
        
        # ... to here.
        assert(mu_new.shape == (self.K, self.D) and               S_new.shape  == (self.K, self.D, self.D) and               pi_new.shape == (self.K, 1))
        return mu_new, S_new, pi_new

    
    def log_likelihood(self, pi, mu, S):
        '''Compute the loglikelihood'''
        
        ll = 0
        for i in range(self.n):
                s = 0
                for k in range(K):
                    s += pi[k] * mvn.pdf((self.X)[i], mu[k], S[k], allow_singular=True)
                ll += np.log(s)
        return -ll
    
    def train(self, initial_params):
        """Fit a Gaussian Mixture Model (GMM) to the data in matrix X.

        Arguments:
          initial_params -- dictionary with fields 'mu', 'S', 'pi' and 'K'

        Returns:kernel 
          mu -- component means, K x D array
          S -- component covariances, K x D x D array
          pi -- component weights, K x 1 array
          r -- component responsabilities, N x K array
        """
        # Assert that initial_params has all the necessary fields
        assert(all([k in initial_params for k in ['mu', 'S', 'pi']]))

        mu = np.zeros((self.K, self.D))
        S  = np.zeros((self.K, self.D, self.D))
        pi = np.zeros((self.K, 1))
        r  = np.zeros((self.n, self.K))

        # Task 3: implement the EM loop to train the GMM
        # Write your code from here...
        
        # updating log likelihoood
        eps = 1e-6  
        K = initial_params['K']
        mu = initial_params['mu']
        S = initial_params['S']
        pi = initial_params['pi']
        
        ll = 1
        previous_ll = 0
        
        while(np.abs(ll-previous_ll) > eps):       
            previous_ll = self.log_likelihood(pi, mu, S)
            
            r = self.E_step(mu, S, pi)
            mu, S, pi =  self.M_step(mu, r)
            ll = self.log_likelihood(pi, mu, S)

        # ... to here.
        assert(mu.shape == (self.K, self.D) and               S.shape  == (self.K, self.D, self.D) and               pi.shape == (self.K, 1) and               r.shape  == (self.n, self.K))
        return mu, S, pi, r


if __name__ == '__main__':
    np.random.seed(43)

    ##########################
    # You can put your tests here - marking
    # will be based on importing this code and calling
    # specific functions with custom input.
    # Do not write code outside the class definition or
    # this if-block.
    ##########################

