#python 3

import numpy as np
import matplotlib.pyplot as plt
#~N(145000, 15000) with 10000 data points
incomes = np.random.normal(145000, 15000, 10000)

plt.hist(incomes,50)    #50 bins
plt.show()
np.median(incomes)

#adding Donald Trump
incomes = np.append(incomes, [1000000000])
print(np.median(incomes))
print(np.mean(incomes))

#creating a random sample of 500 people, age 18-100, all in int
ages = np.random.randint(18,high = 100, size=500)
#print(ages)


from scipy import stats
modes = stats.mode(ages)    #output (value, number of occurence)
print(modes)


#######################################################################

incomes = np.random.normal(100,10,10000)
plt.hist(incomes, 50)   #50 bins
plt.show()
#standard variations and standard deviation functions on np.random.normal
print(incomes.std())
print(incomes.var())

######################################################################
#PDF/PMF: Probability of the data value falling within a certain RV range
#PMF resemble a histogram
#PDF is a continuous function

from scipy.stats import norm
import matplotlib.pyplot as plt

#Uniform Distribution
values = np.random.uniform(-10,10,100000)   #Rx = (-10,10). 100k data points. p=1/(b-a)
plt.hist(values, 100) #note, the number of bins affect our graph
plt.show()

#Normal/Gaussian

xrange = np.arange(-5,5, 0.001) #start, stop, step
plt.plot(xrange, norm.pdf(xrange)) # y ~ N(0,1) of xrange
plt.show()


#General form of Gaussian
mu = 5     #mean
sigma = 2  #stdev
values = np.random.normal(mu,sigma, size=100000)
plt.hist(values, 50)
plt.show()

#Exponential pdf
from scipy.stats import expon
xrange = np.arange(0,10, 0.001)
lambda_ = 4
plt.plot(xrange, expon.pdf(xrange, scale=lambda_)) #y ~exp(lambda)

#binomial pmf
from scipy.stats import binom
n,p = 10, 0.5   #n is the number of bernoulli trials, p = prob of each bern. trial

#pmf plot example
xrange = np.arange(0, 10, 0.001)
plt.plot(xrange, binom.pmf(xrange,n,p))

#Poisson pmf
from scipy.stats import poisson
mu = 500
xrange= np.arange(400, 600, 0.5)
plt.plot(xrange,poisson.pmf(xrange, mu))

##############################################################################
#percentiles and moments

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp

values = np.random.normal(0,1,1000) # N(0,1)

plt.hist(values, 50)
plt.show()

#show X values that represents the cut off percentiles
print(np.percentile(values, 25))
print(np.percentile(values, 50))
print(np.percentile(values, 75))

values = np.random.normal(0, 1, 10000)
plt.hist(values,50)
plt.show()

#moment of 1, 2, 3, 4
m1 = np.mean(values)    #should be 0 for N(0,1)
m2 = np.var(values)     #should be 1 for N(0,1)
m3 = sp.skew(values)    #should be 0 for N(0,1)
m4 = sp.kurtosis(values)#should be 0 for N(0,1)

print(m1,m2,m3,m4)