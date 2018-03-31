#python 3


#%matplotlib inline
import numpy as np
import pandas as pd

df = pd.read_csv("PastHires.csv")

#functions to help view data
df.head(5)      #seeing top 5 rows
df.tail(4)      #seeing bottom 4 rows
df.shape        #shape/dimensions of the dataframe
df.size         #total elements (including NAN) of the dataframe
len(df)         #number of columns
df.columns      #return the column names of our dataframe
df["Hired"]     #selecting the column with name: "Hired"
df["Hired"][:5] #seclecting column "Hired", up to the first 5 rows (slicing)
df["Hired"][5]  #slicing column "Hired" and 5th row
df[["Years Experience", "Hired"]]   #query by 2 columns only
df[["Years Experience", "Hired"]][:5]   #query by 2 columns only, slicing up to 5th row
df.sort_values(["Years Experience"])     #sorting rows based on the column's name
degree_counts = df["Level of Education"].value_counts() #only unique values in the column counted
degree_counts.plot(kind='bar')  #supporting plot function via matplotlib.
