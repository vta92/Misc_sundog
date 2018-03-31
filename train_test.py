# python 3
# basic testing techniques with rsquared eval of MSE

import numpy as np
import matplotlib.pyplot as plt
import sklearn.model_selection
np.random.seed(0)
from sklearn.metrics import r2_score

def plotting(x,y):
    plt.scatter(x,y)
    plt.xlabel('page speed')
    plt.ylabel('purchase amount')
    plt.legend()
    plt.show()

page_speeds = np.random.normal(20,2,1000)
purchase_amount= np.random.normal(100, 2, 1000)/page_speeds
#adding randomness in our inversely proportional relationship

plotting(page_speeds, purchase_amount)
plt.close()


x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(page_speeds, purchase_amount, test_size=0.2)

#plotting(x_train,y_train)
#plotting(x_test, y_test)

#polynomial model for 1 variables
#basically, we evaluate thy hypothesis based on a given single x value
model = np.poly1d(np.polyfit(x_train,y_train,deg = 3))

x = np.linspace(0,30, 1000)
plotting(x, model(x))
plotting(x_test, y_test)


#evaluation, r^2 for our hypothesis against target
r2 = r2_score(y_test, model(x_test))
print(r2)