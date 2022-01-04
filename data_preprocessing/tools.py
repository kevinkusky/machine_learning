# Importing Libraries

import numpy as np
# import matplotlib.pyplot as plt
import pandas as pd

# import data set with pandas

dataset = pd.read_csv('Data.csv')

# Features: Independent Variables - Columns of Data used to predict
#     iloc[rows:range, col:range]
#        example is every row and all but the last column
x = dataset.iloc[:, :-1].values
# [['France' 44.0 72000.0]
#  ['Spain' 27.0 48000.0]
#  ['Germany' 30.0 54000.0]
#  ['Spain' 38.0 61000.0]
#  ['Germany' 40.0 nan]
#  ['France' 35.0 58000.0]
#  ['Spain' nan 52000.0]
#  ['France' 48.0 79000.0]
#  ['Germany' 50.0 83000.0]
#  ['France' 37.0 67000.0]]

# Dependent Variables: Predicted Future Outcomes
#        example is every row and only the last column
y = dataset.iloc[:, -1].values
# ['No' 'Yes' 'No' 'No' 'Yes' 'Yes' 'No' 'Yes' 'No' 'Yes']

print(x)
print(y)


