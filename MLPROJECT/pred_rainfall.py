from sklearn.model_selection import train_test_split
import pandas as pd
import sklearn
from sklearn import linear_model 
data=pd.read_csv('rainfall in india 1901-2015.csv');
print(data.shape)

X=data[['YEAR']]
y=data['ANNUAL']
print(y)
X=X.values.reshape(-1,1) #For Reshaping 
print(X)

import numpy as np
print('unique Values:',np.unique(y))#it can be iterable
y.remove('NAN')

