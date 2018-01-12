import pandas as pd
from sklearn.preprocessing import OneHotEncoder,LabelEncoder

#read data set

dataset = pd.read_csv('city.csv')
#print(dataset)

X = dataset.iloc[:,:-1].values
y = dataset.iloc[:,3].values
#print(X)
#print(y)

#handling missing values
'''
here we are converting all nan value 
imputer will fill all NaN value into total mean average value
'''
from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values='NaN',strategy="mean",axis=0)
imputer = imputer.fit(X[:,1:3])
X[:,1:3] = imputer.fit_transform(X[:,1:3])
#print(X)

'''
here we are using lanbel encoder and one hot encoder 
that will convert all string value into numric values
'''
labelencoder = LabelEncoder()
X[:,0] = labelencoder.fit_transform(X[:,0])
#print(X)

onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()
#print(X)

y = labelencoder.fit_transform(y)
