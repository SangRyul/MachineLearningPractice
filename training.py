# -*- coding: utf-8 -*-
"""
Created on Fri May 19 20:01:58 2017

@author: ksl97
"""

import math
import pandas as pd
import numpy
from sklearn.neighbors import KNeighborsRegressor
from numpy.random import permutation


data = pd.read_csv('colon.csv',index_col=None)


x_columns = data.columns.values
x_columns = numpy.delete(x_columns, 2000,0)


# The column tha1 we want to predict.
y_column = ["class"]


#random_indices = permutation(data.index)
test_cutoff = math.floor(len(data)/9)

random_indices = permutation(data.index)


#랜덤 위치 섞이
test = data.loc[random_indices[1:test_cutoff]]
train = data.loc[random_indices[test_cutoff:]]



knn= KNeighborsRegressor(n_neighbors=10)
# Fit the model on the training data.
knn.fit(train[x_columns], train[y_column])
# Make point predictions on the test set using the fit model.
predictions = knn.predict(test[x_columns])

print(test[y_column])
actual = test[y_column]

# Compute the mean squared error of our predictions.
mse = (((predictions - actual) ** 2).sum()) / len(predictions)

print(float(mse))


