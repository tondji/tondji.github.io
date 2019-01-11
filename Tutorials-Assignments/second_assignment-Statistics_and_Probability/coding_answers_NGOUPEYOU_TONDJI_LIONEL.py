# -*- coding: utf-8 -*-

import numpy as np

############################# q1a     
def postD(nTotal, nWhite):
    #Theta
    N = 10 #Total number of ball available in the bag
    Theta = np.array([i for i in range(N+1)])
    
    # Define the posterior
    
    prior = np.ones(N+1)/(N+1)

    
    #The parameter p for the binomial distribution
    T = Theta/N

    #Computing the factorial
    fact_nTotal = 1
    for i in range(nTotal):
        fact_nTotal = fact_nTotal * (i+1)

    fact_nWhite = 1
    for i in range(nTotal):
        fact_nWhite = fact_nWhite * (i+1)

    fact_nTotal_nWhite = 1
    for i in range(nTotal - nWhite):
        fact_nTotal_nWhite = fact_nTotal_nWhite * (i+1)
    
    
    #Likelihood
    Likelihood = (fact_nTotal/(fact_nWhite * fact_nTotal_nWhite))*(T**(nWhite))*((1-T)**(nTotal-nWhite))
    
    #Evidence
    Evidence = sum(prior*Likelihood)
    
    #Posterior
    Posterior = (prior*Likelihood)/Evidence

    
    return Posterior

############################# q1b      
def evidenceC(nTotal, nWhite):
    #Theta
    N = 10  #Total number of ball available in the bag
    Theta = np.array([i for i in range(N+1)])
    
    # Define the posterior
    
    prior = np.array([1/6,0,1/6,0,1/6,0,1/6,0,1/6,0,1/6])
    #print('The sum over the prior is', sum(prior))
    
    #The parameter p for the binomial distribution
    T = Theta/N

    #Computing the factorial
    fact_nTotal = 1
    for i in range(nTotal):
        fact_nTotal = fact_nTotal * (i+1)

    fact_nWhite = 1
    for i in range(nTotal):
        fact_nWhite = fact_nWhite * (i+1)

    fact_nTotal_nWhite = 1
    for i in range(nTotal - nWhite):
        fact_nTotal_nWhite = fact_nTotal_nWhite * (i+1)
    
    #Likelihood
    Likelihood = (fact_nTotal/(fact_nWhite * fact_nTotal_nWhite))*(T**(nWhite))*((1-T)**(nTotal-nWhite))
    
    #Evidence
    Evidence = sum(prior*Likelihood)

    return Evidence
