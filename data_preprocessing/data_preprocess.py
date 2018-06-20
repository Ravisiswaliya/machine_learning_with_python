import pandas as pd
from sklearn.preprocessing import Imputer,OneHotEncoder,LabelEncoder

#loading dataset
dataset = pd.read_csv('city.csv')

X = dataset.iloc[:,:-1].values  # 0 to 3 column as x
#print(X)
y = dataset.iloc[:,3].values   # selecting last column as y
#print(y)


#handling missing value
imputer = Imputer(missing_values="NaN",strategy='mean',axis=0)
X[:,1:3] = imputer.fit_transform(X[:,1:3])

#labeling
labelencoder = LabelEncoder()
X[:,0] = labelencoder.fit_transform(X[:,0])
#print(X)
y = labelencoder.fit_transform(y)

onehotencoder = OneHotEncoder(categorical_features=[0])
X = onehotencoder.fit_transform(X).toarray()
print(X)

