#python 3

#Correlation and Covariance simple implementation
import numpy as np
from pylab import *

def de_mean(x):
    xmean = mean(x)
    result = [i - xmean for i in x] #deviation from the men for each data pt
    return result

#to evaluate cov, we do dot product between x,y.
#still not normalized to stdev(x) *stdev(y)
def covariance(x,y):
    n= len(x)
    return dot(de_mean(x), de_mean(y))/(n-1)

page_speed = np.random.normal(5,1,100)
purchase_amount = np.random.normal(100,2,100)

#should not correlate, high number due to no normalization
plt = scatter(page_speed, purchase_amount)
print(covariance(page_speed, purchase_amount))

#normalized
print(covariance(page_speed, purchase_amount)/(np.std(page_speed)*np.std(purchase_amount)))

#from numpy library
#matrix is: Cov (x,x), cov(xy), cov(y,x), cov(y,y)
print(np.corrcoef(page_speed,purchase_amount))