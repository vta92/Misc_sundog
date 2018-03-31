#python 3

from numpy import random
import matplotlib.pyplot as plt
random.seed(0)

#total people in an age group
#total purchases in an age group
#initialization
total = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
purchases = {20:0, 30:0, 40:0, 50:0, 60:0, 70:0}
total_purchases = 0

for _ in range(100000):
    #randomly choosing an age group for each of the 100k data
    age_decade = random.choice([20,30,40,50,60,70])
    purchase_prob = float(age_decade)/100 #age and prob are linearly related
    #modification in which age and purchases aren't dependent
    #purchase_prob = random.random()
    total[age_decade] += 1
    
    if (random.random() < purchase_prob):    #return a float [0,1)
        total_purchases += 1
        purchases[age_decade] += 1


#computing P(E|F), prob of purchase when that person is in his/her 30s
#due to large n value, it supposed to be close to age_decade/100 as above
prob_pop = float(total[30])
prob_purchase = float(purchases[30])
PEF = prob_purchase/prob_pop
print("P(purchase|30s) = ", str(PEF))

PF = total[30]/100000
print("P(30s) = ", PF)   #n is the number of loops, close to pf = 1/(7-2+1)

#PE is the probability of buying something, regardless of age
PE = float(total_purchases)/100000

#checking dependency: P(30)P(Purchase) ?= P(30,purchase)
print("P(30)P(Purchase)" + str(PE * PF))
print("P(30, Purchase)" + str(float(purchases[30])/100000))
#If they are dependent. 2 print statements don't match

#check the Bayes' Theorem: P(purchase|30) = P(30, Purchase)/P(30)
print((purchases[30] / 100000.0) / PF)

################
#visual of age/purchases
xrange = list()
yrange = list()
for key in purchases:
    xrange.append(key)
    yrange.append(purchases[key])
plt.scatter(xrange, yrange)
plt.xlim(0, 100)
plt.ylim(0, 100000)
plt.xlabel("Age Groups")
plt.ylabel("Count")
plt.show()
