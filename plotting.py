#python 3

#basic
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

xrange = np.arange(-3,3,0.001)
plt.plot(xrange, norm.pdf(xrange))
plt.show()

#multiple plots on 1 graph
mu, sigma = 1,0.5
plt.plot(xrange, norm.pdf(xrange))
plt.plot(xrange, norm.pdf(xrange,mu,sigma))
plt.show()
plt.close()
#plt.savefig("test.png") #to save

#Axis configurations
axes = plt.axes()
#Set x, y limits
axes.set_xlim(-4,4)
axes.set_ylim(0,1)
axes.set_xticks(np.arange(-4,4,0.5)) #input as a list
axes.set_yticks(np.arange(0,1,0.1)) #input as a list
plt.plot(xrange, norm.pdf(xrange,0.0,1.0),'b-')    #quote represents line outputs
plt.plot(xrange, norm.pdf(xrange,1.0,0.5),'r:')
plt.legend(["Test1","Test2"], loc=4)
#axis labels and legend
plt.xlabel("x")
plt.ylabel("Probability")

plt.grid()  #shows grids in graph
plt.show()
plt.close()
###########################################
#Pie Chart

values = [12,55,4,32,14]
colors = ['r','g','b','c','m']
explode = [0,0,0.2,0.1,0.15]    #how to make pie charts pop out
labels = ['India', 'USA','Russia','China','Europe']
plt.pie(values, colors=colors, labels=labels, explode=explode)
plt.title("Diversity")
plt.show()
plt.close()

##########################################
#Bar Chart
values = [12,55,4,32,14]
colors = ['r','g','b','c','m']
plt.bar(range(0,5), values, color=colors)
plt.show()
plt.close()

##########################################
#Scatter Plot
from pylab import randn

xrange = randn(500)
yrange = randn(500)
plt.scatter(xrange,yrange)
plt.show()
plt.close()

##########################################
#Histograms

incomes = np.random.normal(0,1,10000)
plt.hist(incomes, bins=100)
plt.show()
plt.close()

##########################################
#Box and Whisker Plot
uniformSkewed = np.random.rand(100)
high_outliers = np.random.rand(10)*50 + 100  #10 modified data points
low_outliers = np.random.rand(10)*(-50) - 100

#note the double paranthesis
data = np.concatenate((uniformSkewed, high_outliers, low_outliers))
plt.boxplot(data)
plt.show()



