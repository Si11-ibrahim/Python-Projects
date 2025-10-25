print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

import sklearn as sk
from sklearn.linear_model import LogisticRegression
from sklearn.linear_model import LinearRegression
from sklearn.datasets import load_breast_cancer
import numpy as np
import pandas as pd

cancer_data = load_breast_cancer()

print(cancer_data.keys())                       #.keys() argument is used to print the keys of the dataset
        #Output: dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename', 'data_module'])
print('==========================================================================================================')

'''data = cancer_data['data']
print(data.shape)'''                            #.shape attribute is used to count the no. of rows and columns

print('==========================================================================================================')

df = pd.DataFrame(cancer_data['data'], columns = cancer_data['feature_names'])
df['target'] = cancer_data['target']

#print(df.head())                               #.head() argument is used to print the first 5(as default) rows of the dataset. we can also print more like this .head(10)

X = df[cancer_data.feature_names].values        #.values attribute is used to convert dataframe into numpy array
y = df['target'].values


model = LogisticRegression(solver='liblinear')  #solver is the algorithm to find the equation of the line. liblinear is a library.
model.fit(X, y)                                 #.fit method is used to build the model.

print(model.predict([X[0]]))                    #.predict method is used to make predictions
    #Output: 0                                  #Our model's prediction for first datapoint is 0. 0 means malignant
print(model.score(X, y))                        #.score method matches X and y, it counts what percent of them matches and shows it's accuracy score
    #Output: 0.9595782073813708                 #it means our model predicts 96%(95.9) accurately

