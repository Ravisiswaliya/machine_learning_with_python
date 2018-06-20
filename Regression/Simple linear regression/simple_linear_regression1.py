#for removing warning message
import warnings
warnings.filterwarnings(action="ignore", module="scipy", message="^internal gelsd")

#reading data
import pandas as pd
dataset = pd.read_csv('salary.csv')

#dividing data into x and y
x = dataset.iloc[:,0:1].values
y = dataset.iloc[:,-1:].values

#training and testing data
from sklearn.model_selection import train_test_split

x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# selecting algorithm
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(x_train, y_train)

#checking accuracy
accuracy = lr.score(x_test, y_test)
print(accuracy*100)

#predicting based on linear regression
print(lr.predict(8))
for i in range(1,11):
    print(i,'=',lr.predict(i))

#plotting result on graph
import matplotlib.pyplot as plt
plt.scatter(x_train,y_train, color = 'black')
plt.plot(x_test,lr.predict(x_test), color = 'red')
plt.title("Salary vs Experience")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()
