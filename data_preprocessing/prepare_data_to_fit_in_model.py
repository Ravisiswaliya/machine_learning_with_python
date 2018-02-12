from sklearn.preprocessing import LabelEncoder
import pandas as pd

# create dataset
data =  {'country': ['usa','uk', 'singapore', 'india'],
         'rank':[3,2,4,1],
         'language': ['english','english','english','hindi'],}

# setting data kays as heading
df = pd.DataFrame(data, columns=['country','rank','language'])
print(df)
# fit data to labelecoder
le = LabelEncoder()
df['country']=le.fit_transform(df['country'])
df['language']=le.fit_transform(df['language'])

#print data after
print(df)

