
# coding: utf-8

# ## 3) Bayesian Linear Regression

# In[ ]:

import numpy as np


# In[ ]:

def lml(alpha, beta, Phi, Y):
    
    N = Y.shape[0]
    A = alpha * (Phi @ Phi.T) + beta*np.eye(N)
    lml = (-N * np.log(2*np.pi) - np.log(abs(np.linalg.det(A))) - Y.T @ (np.linalg.inv(A+ 1e-08*np.eye(A.shape[0])) @ Y))/2
                                           
    return lml


# In[ ]:

def grad_lml(alpha, beta, Phi, Y):
    
    N = Y.shape[0]
    A = alpha * (Phi @ Phi.T) + beta*np.eye(N)
    
    alpha_grad = (Y.T @ (np.linalg.inv(A) @ Phi @ Phi.T @ np.linalg.inv(A) @ Y) - np.trace(np.linalg.inv(A) @ Phi @ Phi.T))/2
    beta_grad = (Y.T @ (np.linalg.inv(A) @ np.linalg.inv(A)) @ Y - np.trace(np.linalg.inv(A)))/2
    
    return (alpha_grad, beta_grad)

