import pandas as pd
##import Quandl
import math
import numpy as np
#from sklearn import preprocessing, cross_validation, svm
##from sklearn.linear_model import LinearRegression
import pickle
from datetime import datetime



df = pd.read_csv('uberdata.txt')
print('1')
print(df.head())
print(df.dtypes)
df.DateTime.str.slice(-5,-3).astype(int).head()
df['DateTime'] = pd.to_datetime(df.DateTime)
print('2')
print(df.head())
print(df.dtypes)
pi = pd.PeriodIndex(df['DateTime'],freq='s')
p0 = pd.Period('1970-1-1',freq= 's')


df['timeSeconds'] = pi-p0

print(df.head())

df.to_csv('uberunixtime.csv')



#print(df['DateTime'].dt.total_seconds())
#df['timeSeconds'] = df['DateTime'].dt.total_seconds()
##for d in range df:
 ##   a = datetime.strptime(convdate, "%b %d %H:%M:%S %Y %Z")
 ##   b = datetime(1970, 1, 1)
 ##   (a-b).total_seconds()



##df.drop(['Base'], 1, inplace=True)
##print(df.head())
##df.convert_objects(convert_numeric=True).dtypes
##print(df.head())
##df.dropna(inplace=True)


