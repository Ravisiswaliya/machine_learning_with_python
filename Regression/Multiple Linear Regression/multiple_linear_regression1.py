import warnings
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")


import pandas as pd
dataset = pd.read_csv('startup.csv')
#print(dataset)

from sklearn.preprocessing import OneHotEncoder,LabelEncoder
x = dataset.iloc[:,:-1].values
#print(x)
y = dataset.iloc[:,-1:].values
#print(y)

#labeling 3 cloumn of dataset
labelencoder = LabelEncoder()
x[:,3] = labelencoder.fit_transform(x[:,3])
#print(x)
#one hot encoding
onehotencoder = OneHotEncoder(categorical_features=[3])
x = onehotencoder.fit_transform(x).toarray()

x = x[:,1:]
#print(x)
#y = onehotencoder.fit_transform(y)

#spliting data into training and testing
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test  = train_test_split(x,y,test_size=0.2, random_state=0)

#implementing algorithm
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train,y_train)
print(lr.score(x_test,y_test))

#visualization data

import matplotlib.pyplot as plt
print(len(x_train))
print(len(y_train))
plt.scatter(x_train, y_train, color =  'red')
plt.plot(x_train, regressor.predict(x_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

