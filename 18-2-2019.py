#!/usr/bin/env python
# coding: utf-8

# In[8]:


import os
import numpy as np
import pandas as pd

#os.chdir("C:/Users/abbasnam/Downloads/Files")
data = pd.read_csv('C:/Users/abbasnam/Downloads/Files/Campfil_1.csv')
#csvfile = pd.read_csv('C:/Users/abbasnam/Downloads/Files')

print(data)


# In[ ]:


csvFile = 'C:/Users/abbasnam/Downloads/Files/Camfil_1.csv'

def read_csv(csv_file):
    data = []
    with open(csv_file, 'r') as f:

        # create a list of rows in the CSV file
        rows = f.readlines()

        # strip white-space and newlines
        rows = list(map(lambda x:x.strip(), rows))

        for row in rows:

            # further split each row into columns assuming delimiter is comma 
            row = row.split(',')

            # append to data-frame our new row-object with columns
            data.append(row)

    return data


# In[9]:


csvFile = 'C:Users/abbasnam/Downloads/Files/Camfil_1.csv'

data = read_csv(csvFile)


# In[10]:


import csv

f = open('C:\Users\abbasnam\Downloads\Files\Camfil_1.csv', 'rb')
reader = csv.reader(f)
for row in reader:
    print row
f.close()


# In[ ]:


#f = open('C:\Users\abbasnam\Downloads\Files\Camfil_1.csv', 'rb')
#C:\Users\abbasnam\Downloads\Files


# In[11]:


import pandas as pd

# Reading data from csv file
df = pd.read_csv('CamCloseM6 4V300E10', sep=',')
print(df)


# In[ ]:


for x in os.listdir('.'):
    print x


# In[12]:


import pandas as pd

# Reading data from csv file
c


# In[ ]:


df.shape


# In[ ]:


df[0]


# In[13]:


import pandas as pd

# Reading data from csv file
df = pd.read_csv('CamCloseM6 4V300E10.csv', sep=',', delim_whitespace=True, 
                 parse_dates=[0], infer_datetime_format=True)
print(df)


# In[15]:


import pandas as pd
df = pd.read_csv('CamCloseM6 4V300E10.csv', sep=',')
print(df)


# In[ ]:


df.shape


# In[ ]:


df.shape


# In[16]:


import pandas as pd
from datetime import datetime
import csv
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
#headers = ['LocalTime','Duct1\DataStore\DuctDiffPressure','Duct1\DataStore\DuctHumidity']
#df = pd.read_csv('C:/Users\Lala Rushan\Downloads\DataLog.CSV',names=headers)
#print (df)

x = df['LocalTime']
y = df['Duct1\DataStore\DuctDiffPressure']

# plot
plt.plot(x,y)
# beautify the x-labels
plt.gcf().autofmt_xdate()

plt.show()


# In[ ]:


4+2


# In[ ]:


df.shape


# In[ ]:


df.shape


# In[ ]:


5+2


# In[ ]:


df.shape


# In[ ]:


df.sahpe


# In[ ]:


5*2


# In[ ]:


df.shape


# In[ ]:


import pandas as pd

df = pd.read_csv('CamCloseM6 4V300E10.csv', sep=',')
print(df)


# In[ ]:


3+4


# In[ ]:


for x in os.listdir('.'):
    print x


# In[ ]:


import os
for x in os.listdir('.'):
    print x


# In[ ]:


cd


# In[ ]:


ls


# In[ ]:


cd Downloads/


# In[ ]:


ls


# In[ ]:


cd 


# In[17]:


import os
os.getcwd()


# In[18]:


os.chdir('C:\Users\abbasnam')


# In[19]:


import os
os.chdir('C:\Users\abbasnam')


# In[21]:


import os
os.chdir('C:/Users/abbasnam')


# In[22]:


os.getcwd()


# In[23]:


for x in os.listdir('.'):
    print x


# In[24]:


cd Downloads/


# In[ ]:


for x in os.listdir('.'):
    print x


# In[25]:


cd Files/


# In[26]:


for x in os.listdir('.'):
    print x


# In[27]:


import pandas as pd

data = pd.read_csv('CamCloseM6 4V300E10.csv', sep=',')
print(data)


# In[28]:


data.shape


# In[29]:


#retrieves rows of data and saves it as a list of list
x = [row for row in data]



# In[30]:


print x


# In[31]:


x.shape


# In[32]:


data.shape


# In[33]:


int_x = np.array(x, int)


# In[34]:


import numpy as np

int_x = np.array(x, int)


# In[35]:


import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
get_ipython().magic(u'matplotlib inline')



# In[36]:


data.head()


# In[37]:


data.describe()


# In[38]:


data.plot(x='LocalTime', y='Duct1\DataStore\DuctDiffPressure', style='o')  
plt.title('Time vs Pressure')  
plt.xlabel('LocalTim')  
plt.ylabel('Duct1\DataStore\DuctDiffPressure')  
plt.show() 


# In[39]:


import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
get_ipython().magic(u'matplotlib inline')

data.plot(x='LocalTime', y='Duct1\DataStore\DuctDiffPressure', style='o')  
plt.title('Time vs Pressure')  
plt.xlabel('LocalTim')  
plt.ylabel('Duct1\DataStore\DuctDiffPressure')  
plt.show() 


# In[40]:


X = data.iloc[:, :-1].values


# In[41]:


print X


# In[42]:


y = data.iloc[:, 1].values


# In[43]:


print y


# In[44]:


from sklearn.model_selection import train_test_split  

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0) 


# In[ ]:


5+6


# In[ ]:


X_train


# In[ ]:


y_train


# In[ ]:


from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(X_train, y_train)  


# In[ ]:


regressor


# In[ ]:


regressor.fit(X_train, y_train) 


# In[ ]:


print(regressor.intercept_) 


# In[ ]:


print(regressor.coef_)


# In[ ]:


y_pred = regressor.predict(X_test)


# In[ ]:


import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
get_ipython().magic(u'matplotlib inline')

data.plot(x='LocalTime', y='Duct1\DataStore\DuctDiffPressure', style='o')  
plt.title('Time vs Pressure')  
plt.xlabel('LocalTim')  
plt.ylabel('Duct1\DataStore\DuctDiffPressure')  
plt.show() 


# In[45]:


data.shape


# In[46]:


data.shape


# In[47]:


a = data[0:]


# In[48]:


print a


# In[49]:


import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
get_ipython().magic(u'matplotlib inline')

data.plot(x='LocalTime', y='Duct1\DataStore\DuctDiffPressure', style='o')  
plt.title('Time vs Pressure')  
plt.xlabel('LocalTim')  
plt.ylabel('Duct1\DataStore\DuctDiffPressure')  
plt.show() 


# In[50]:


import plotly.graph_objs as go
fig = go.FigureWidget()
# Display an empty figure
fig


# In[51]:


# Add a scatter chart
fig.add_scatter(y=[2, 1, 4, 3])
# Add a bar chart
fig.add_bar(y=[1, 4, 3, 2])
# Add a title
fig.layout.title = 'Hello FigureWidget'


# In[52]:


x='LocalTime',
y='Duct1\DataStore\DuctDiffPressure'

fig.add_scatter(x)


# In[53]:


data.head()


# In[54]:


import csv
for row in csv.reader(data):
    print row


# In[55]:


import csv
for row in csv.reader(data):
    print row[0]


# In[56]:


import csv
for column in csv.reader(data):
    print column[-1]


# In[57]:


col_2 = list(zip(*data))[1] # keeping in mind that python is 0-indexed


# In[58]:


print col_2


# In[59]:


col_2 = list(zip(*data))[0]
print col_2


# In[ ]:


col_2 = [x[1] for x in data]

print col_2


# In[60]:


col_2 = [x[3] for x in data]

print col_2


# In[61]:


import pandas as pd
#headers = data.fieldnames

for line in data:
    #print value in MyCol1 for each row
    print(line[:])


# In[62]:


line[0]


# In[63]:


data.head()


# In[64]:


import pandas as pd

data = pd.read_csv('CamCloseM6 4V300E10.csv', sep=',' ,parse_dates=True,keep_date_col = True)
print(data)


# In[65]:


parse_dates


# In[ ]:


data


# In[66]:


LocalDate = data['LocalDate']


# In[67]:


LocalTime = data['LocalTime']


# In[68]:


DiffPressure = data['Duct1\DataStore\DuctDiffPressure']


# In[69]:


Temperature = data['Duct1\DataStore\DuctTemperature']


# In[70]:


Humidity = data['Duct1\DataStore\DuctHumidity']


# In[71]:


Velocity = data['Duct1\DataStore\DuctVelocity']


# In[72]:


DustTrack = data['Duct1\DataStore\DustTrack']


# In[73]:


from numpy import *
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

LocalDate = data['LocalDate']
LocalTime = data['LocalTime']
DiffPressure = data['Duct1\DataStore\DuctDiffPressure']
Temperature = data['Duct1\DataStore\DuctTemperature']
Humidity = data['Duct1\DataStore\DuctHumidity']
Velocity = data['Duct1\DataStore\DuctVelocity']
DustTrack = data['Duct1\DataStore\DustTrack']

plt.plot(DiffPressure, Humidity, Velocity, DustTrack)
plt.show()


# In[74]:


from numpy import *
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

LocalDate = data['LocalDate']
LocalTime = data['LocalTime']
DiffPressure = data['Duct1\DataStore\DuctDiffPressure']
Temperature = data['Duct1\DataStore\DuctTemperature']
Humidity = data['Duct1\DataStore\DuctHumidity']
Velocity = data['Duct1\DataStore\DuctVelocity']
DustTrack = data['Duct1\DataStore\DustTrack']

fig = plt.figure()
ax = plt.subplot(111)
ax.plot(DiffPressure, Humidity, Velocity, DustTrack)
ax.legend()
plt.show()


# In[75]:


ax = Humidity.plot(figsize=(20,10))
DustTrack.plot(ax=ax)
Temperature.plot(ax=ax)


# In[76]:


ax = Humidity.plot(figsize=(20,10))
DustTrack.plot(ax=ax)
Temperature.plot(ax=ax)


# In[77]:


ax = Humidity.plot(figsize=(20,10))
DustTrack.plot(ax=ax)
Temperature.plot(ax=ax)
DiffPressure.plot(ax=ax)
ax.legend()


# In[78]:


Humidity = Humidity.plot(figsize=(20,10))
Humidity.legend()


# In[79]:


Temperature = Temperature.plot(figsize=(20,10))


# In[80]:


DiffPressure = DiffPressure.plot(figsize=(20,10))


# In[81]:


DustTrack = DustTrack.plot(figsize=(20,10))


# In[82]:


DustTrack = DustTrack.plot(figsize=(20,10))


# In[83]:


Velocity


# In[84]:


DustTrack


# In[85]:


DustTrack = data['Duct1\DataStore\DustTrack']


# In[86]:


DustTrack


# In[87]:


DustTrack = DustTrack.plot(figsize=(20,10))
ax.grid(True)


# In[88]:


data.index


# In[89]:


data.columns


# In[90]:


data.head()


# In[91]:


data.columns


# In[93]:


data.head(10)


# In[96]:


data.head()


# In[97]:


data.shape


# In[99]:


data.shape[0]


# In[100]:


data.info


# In[101]:


data.info()


# In[104]:


data.columns


# In[105]:


data.index


# In[107]:


c = data.groupby('Duct1\DataStore\DuctDiffPressure')


# In[108]:


print c


# In[110]:


c = c.sum()
print c


# In[111]:


c.head(1)


# In[112]:


data.describe(include = "all")


# In[113]:


data.head()


# In[115]:


LocalDate = data['LocalDate']
print LocalDate 


# In[116]:


LocalTime = data['LocalTime']
print LocalDate 


# In[118]:


DiffPressure = data['Duct1\DataStore\DuctDiffPressure']
print DiffPressure


# In[119]:


Temperature = data['Duct1\DataStore\DuctTemperature']
print DiffPressure


# In[120]:


Humidity = data['Duct1\DataStore\DuctHumidity']
print Humidity


# In[121]:


DustTrack = data['Duct1\DataStore\DustTrack']
print DustTrack


# In[122]:


max (DustTrack)


# In[123]:


min (DustTrack)


# In[126]:


data.sort_values()


# In[127]:


data.items


# In[136]:





# In[139]:


plt.hist(data['Duct1\DataStore\DustTrack'].dropna())


# In[140]:


data['Duct1\DataStore\DustTrack'].corr(data['Duct1\DataStore\DuctDiffPressure'])


# In[142]:


data['Duct1\DataStore\DuctTemperature'].corr(data['Duct1\DataStore\DuctDiffPressure'])


# In[143]:


data['Duct1\DataStore\DuctHumidity'].corr(data['Duct1\DataStore\DuctDiffPressure'])


# In[145]:


Velocity = Velocity.plot(figsize=(20,10))
ax.grid(True)

#Velocity = data['Duct1\DataStore\DuctVelocity']


# In[1]:


data


# In[1]:


pwd


# In[2]:


import os

os.listdir


# In[3]:


os.listdir()


# In[6]:


os.listdir('C:\Users\abbasnam\Downloads\Files')


# In[5]:


os.getcwd()


# In[7]:


pwd


# In[8]:


path = os.getcwd()


# In[12]:





# In[13]:


os.listdir('C:\\Users\\abbasnam')


# In[14]:


import os
os.listdir(os.getcwd())


# In[16]:


import os, sys

#open files in directory

path = "C:"
dirs = os.listdir(path)

# print the files in given directory

for file in dirs:
   print (file)


# In[17]:


cd c:Downloads/


# In[18]:


cd


# In[19]:


cd


# In[20]:


cd ..


# In[21]:


import os, sys

#open files in directory

path = "C:\Users"
dirs = os.listdir(path)

# print the files in given directory

for file in dirs:
   print (file)


# In[22]:


cd abbasnam/


# In[23]:


import os, sys

#open files in directory

path = "C:\Users\abbasnam"
dirs = os.listdir(path)

# print the files in given directory

for file in dirs:
   print (file)


# In[26]:


pwd


# In[28]:


import os, sys

#open files in directory

path = "C:\\Users\\abbasnam"
dirs = os.listdir(path)

# print the files in given directory

for file in dirs:
   print (file)


# In[29]:


cd


# In[30]:


cd C:\Users\abbasnam\Downloads\Files


# In[31]:


os.listdir()


# In[32]:


pwd


# In[34]:


path = "C:\\Users\\abbasnam\\Downloads\\Files"
dirs = os.listdir(path)
print dirs


# In[35]:


import pandas as pd

data = pd.read_csv('CamCloseM6 4V300E10.csv', sep=',' ,parse_dates=True,keep_date_col = True)
print(data)


# In[36]:


data.head()


# In[40]:


import matplotlib as plt 

Pressure = data['Duct1\DataStore\DuctDiffPressure']

print Pressure


# In[52]:


data.describe


# In[59]:


from numpy import *
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

#LocalDate = data['LocalDate']
#LocalTime = data['LocalTime']
DiffPressure = data['Duct1\DataStore\DuctDiffPressure']
#Temperature = data['Duct1\DataStore\DuctTemperature']
#Humidity = data['Duct1\DataStore\DuctHumidity']
#Velocity = data['Duct1\DataStore\DuctVelocity']
#DustTrack = data['Duct1\DataStore\DustTrack']

#fig = plt.figure()
#ax = plt.subplot(111)
#ax.plot(DiffPressure#, Humidity, Velocity, DustTrack  
#       )
#ax.legend()
#plt.show()


DiffPressure = DiffPressure.plot(figsize=(20,10))
#DiffPressure.plot(ax=ax)
#Temperature.plot(ax=ax)
DiffPressure.legend()


# In[62]:


# Code source: Jaques Grobler

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Use only one feature
Humidity_X = data['Duct1\DataStore\DuctHumidity']

# Split the data into training/testing sets

Humidity_X_train = Humidity_X[:-20]
Humidity_X_test = Humidity_X[-20:]

# Split the targets into training/testing sets

#DiffPressure_y_train = DiffPressure.target[:-20]
#DiffPressure_y_test = DiffPressure.target[-20:]

# Create linear regression object

#regr = linear_model.LinearRegression()

# Train the model using the training sets
#regr.fit(Humidity_X_train, DiffPressure_y_test)

# Make predictions using the testing set
#diabetes_y_pred = regr.predict(diabetes_X_test)

# The coefficients
#print('Coefficients: \n', regr.coef_)
# The mean squared error
#print("Mean squared error: %.2f"
#      % mean_squared_error(diabetes_y_test, diabetes_y_pred))
# Explained variance score: 1 is perfect prediction
#print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

# Plot outputs
#plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
#plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

#plt.xticks(())
#plt.yticks(())

#plt.show()


# In[63]:


print Humidity_X_train


# In[64]:


Humidity_X_train.shape


# In[65]:


print Humidity_X_test


# In[75]:


from sklearn.model_selection import train_test_split

Humidity = data['Duct1\DataStore\DuctHumidity']

trainingSet, testSet = train_test_split(Humidity, test_size=0.2)



#X_train, X_test, y_train, y_test 
#= train_test_split(Humidity_X, y, test_size=0.2, random_state=1)


# In[ ]:


"""
Created on Thu Mar 22 07:29:29 2018

@author: Pawanvir Singh

This is minimal Example of Polynomial 
Regression with One Variable 

as we Know when we add polynomial terms to 
Our regression hypothesis  the function will no more linear 
so it will lead to better fit our model to non linear data set
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from sklearn.linear_model import LinearRegression

#loading the dataset

dataset= pd.read_csv("../input/Position_Salaries.csv")
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, -1].values

#adding Polynomial for better fitting of data 

from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree= 2)
poly_features = poly.fit_transform(X)
poly.fit(X,y)
poly_regression = LinearRegression()
poly_regression.fit(poly_features,y)

#normal regression

regressor=LinearRegression()
regressor.fit(X,y)
#ploting the data  

plt.scatter(X,y)
plt.plot(X,poly_regression.predict(poly_features))
plt.title("PolyNomial Regression Experiance Vs Salary with degree 2 ")
plt.xlabel("Experiance ")
plt.ylabel("Salary data ")
plt.show()
#plotting linear hypothesis
plt.scatter(X,y)
plt.plot(X,regressor.predict(X))
plt.title("Linear  Regression Experiance Vs Salary  ")
plt.xlabel("Experiance ")
plt.ylabel("Salary data ")
plt.show() 
# higher degree
# Adding Polynominals to the hypothesis 
poly = PolynomialFeatures(degree= 3)
poly_features = poly.fit_transform(X)
poly.fit(X,y)
poly_regression = LinearRegression()
poly_regression.fit(poly_features,y)
#ploting the data  for polynomial regression 
plt.scatter(X,y)
plt.plot(X,poly_regression.predict(poly_features))
plt.title("PolyNomial Regression Experiance Vs Salary with degree 3 ")
plt.xlabel("Experiance ")
plt.ylabel("Salary data ")
plt.show()
#ploting the Linear regresson
plt.scatter(X,y)
plt.plot(X,regressor.predict(X))
plt.title("Linear  Regression Experiance Vs Salary  ")
plt.xlabel("Experiance ")
plt.ylabel("Salary data ")
plt.show() 


# In[76]:


from sklearn.model_selection import train_test_split

Humidity = data['Duct1\DataStore\DuctHumidity']

trainingSet, testSet = train_test_split(Humidity, test_size=0.2)



#X_train, X_test, y_train, y_test 
#= train_test_split(Humidity_X, y, test_size=0.2, random_state=1)


# In[77]:


print trainingSet, testSet


# In[78]:


shape (testSet)


# In[79]:


shape (trainingSet)


# In[80]:


trainingSet.describe()


# In[81]:


testSet.describe()


# In[85]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy import stats
from scipy.stats import norm
from scipy.stats import binned_statistic
import warnings
warnings.filterwarnings('ignore')
get_ipython().magic(u'matplotlib inline')

#sns.heatmap(testSet.corr(), vmax=.8, square=True);
corrmat = testSet.corr()


# In[89]:


testSet = pd.DataFrame(testSet)


# In[91]:


testSet.corr()

sns.pairplot(testSet)


# In[93]:


import matplotlib.pyplot as plt

plt.matshow(testSet.corr())


# In[95]:


sns.heatmap(testSet.corr(), vmax=.8, square=True);


# In[96]:


data.head()


# In[99]:


sns.heatmap(data.corr(), vmax=.8, square=True);


# In[102]:


arr_train_cor = data.corr()['Duct1\DataStore\DuctDiffPressure']
print arr_train_cor


# In[ ]:





# In[ ]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from sklearn.linear_model import LinearRegression


#loading the dataset

from sklearn.model_selection import train_test_split

DiffPressure = data['Duct1\DataStore\DuctDiffPressure']

trainingSet, testSet = train_test_split(DiffPressure, test_size=0.2)

#adding Polynomial for better fitting of data 

from sklearn.preprocessing import PolynomialFeatures

poly = PolynomialFeatures(degree= 2)     # we start with second order, we can try 3 ,... (Justif)
poly_features = poly.fit_transform(X)
poly.fit(X,y)
poly_regression = LinearRegression()
poly_regression.fit(poly_features,y)


# In[103]:


print data


# In[ ]:


#!/usr/bin/env python
# Implementation of algorithm from https://stackoverflow.com/a/22640362/6029703
import numpy as np
import pylab

def thresholding_algo(y, lag, threshold, influence):
    signals = np.zeros(len(y))
    filteredY = np.array(y)
    avgFilter = [0]*len(y)
    stdFilter = [0]*len(y)
    avgFilter[lag - 1] = np.mean(y[0:lag])
    stdFilter[lag - 1] = np.std(y[0:lag])
    for i in range(lag, len(y)):
        if abs(y[i] - avgFilter[i-1]) > threshold * stdFilter [i-1]:
            if y[i] > avgFilter[i-1]:
                signals[i] = 1
            else:
                signals[i] = -1

            filteredY[i] = influence * y[i] + (1 - influence) * filteredY[i-1]
            avgFilter[i] = np.mean(filteredY[(i-lag+1):i+1])
            stdFilter[i] = np.std(filteredY[(i-lag+1):i+1])
        else:
            signals[i] = 0
            filteredY[i] = y[i]
            avgFilter[i] = np.mean(filteredY[(i-lag+1):i+1])
            stdFilter[i] = np.std(filteredY[(i-lag+1):i+1])

    return dict(signals = np.asarray(signals),
                avgFilter = np.asarray(avgFilter),
                stdFilter = np.asarray(stdFilter))


# In[104]:


# Data
y = np.array([1,1,1.1,1,0.9,1,1,1.1,1,0.9,1,1.1,1,1,0.9,1,1,1.1,1,1,1,1,1.1,0.9,1,1.1,1,1,0.9,
       1,1.1,1,1,1.1,1,0.8,0.9,1,1.2,0.9,1,1,1.1,1.2,1,1.5,1,3,2,5,3,2,1,1,1,0.9,1,1,3,
       2.6,4,3,3.2,2,1,1,0.8,4,4,2,2.5,1,1,1])


# In[105]:


print y


# In[107]:


type(y)


# In[108]:


shape(y)


# In[109]:


# Settings: lag = 30, threshold = 5, influence = 0
lag = 30
threshold = 5
influence = 0

# Run algo with settings from above
result = thresholding_algo(y, lag=lag, threshold=threshold, influence=influence)


# In[111]:


import numpy as np
import pylab

def thresholding_algo(y, lag, threshold, influence):
    signals = np.zeros(len(y))
    filteredY = np.array(y)
    avgFilter = [0]*len(y)
    stdFilter = [0]*len(y)
    avgFilter[lag - 1] = np.mean(y[0:lag])
    stdFilter[lag - 1] = np.std(y[0:lag])
    for i in range(lag, len(y)):
        if abs(y[i] - avgFilter[i-1]) > threshold * stdFilter [i-1]:
            if y[i] > avgFilter[i-1]:
                signals[i] = 1
            else:
                signals[i] = -1

            filteredY[i] = influence * y[i] + (1 - influence) * filteredY[i-1]
            avgFilter[i] = np.mean(filteredY[(i-lag+1):i+1])
            stdFilter[i] = np.std(filteredY[(i-lag+1):i+1])
        else:
            signals[i] = 0
            filteredY[i] = y[i]
            avgFilter[i] = np.mean(filteredY[(i-lag+1):i+1])
            stdFilter[i] = np.std(filteredY[(i-lag+1):i+1])

    return dict(signals = np.asarray(signals),
                avgFilter = np.asarray(avgFilter),
                stdFilter = np.asarray(stdFilter))




# Settings: lag = 30, threshold = 5, influence = 0
lag = 30
threshold = 5
influence = 0

# Run algo with settings from above
result = thresholding_algo(y, lag=lag, threshold=threshold, influence=influence)
print result 


# In[112]:


data


# In[113]:


DiffPressure = data['Duct1\DataStore\DuctDiffPressure']


# In[114]:


DiffPressure = np.(DiffPressure)


# In[115]:


type(DiffPressure)


# In[116]:


DiffPressure = pd.to_numeric(DiffPressure, downcast='float')


# In[117]:


type (DiffPressure)


# In[118]:


print DiffPressure


# In[119]:


DiffPressure = DiffPressure.values


# In[120]:


type (DiffPressure)


# In[121]:


print (DiffPressure)


# In[122]:


shape(DiffPressure )


# In[123]:


import numpy as np
import pylab

def thresholding_algo(y, lag, threshold, influence):
    signals = np.zeros(len(y))
    filteredY = np.array(y)
    avgFilter = [0]*len(y)
    stdFilter = [0]*len(y)
    avgFilter[lag - 1] = np.mean(y[0:lag])
    stdFilter[lag - 1] = np.std(y[0:lag])
    for i in range(lag, len(y)):
        if abs(y[i] - avgFilter[i-1]) > threshold * stdFilter [i-1]:
            if y[i] > avgFilter[i-1]:
                signals[i] = 1
            else:
                signals[i] = -1

            filteredY[i] = influence * y[i] + (1 - influence) * filteredY[i-1]
            avgFilter[i] = np.mean(filteredY[(i-lag+1):i+1])
            stdFilter[i] = np.std(filteredY[(i-lag+1):i+1])
        else:
            signals[i] = 0
            filteredY[i] = y[i]
            avgFilter[i] = np.mean(filteredY[(i-lag+1):i+1])
            stdFilter[i] = np.std(filteredY[(i-lag+1):i+1])

    return dict(signals = np.asarray(signals),
                avgFilter = np.asarray(avgFilter),
                stdFilter = np.asarray(stdFilter))




# Settings: lag = 30, threshold = 5, influence = 0
lag = 30
threshold = 5
influence = 0

# Run algo with settings from above

y = DiffPressure

result = thresholding_algo(y, lag=lag, threshold=threshold, influence=influence)
print result 


# In[124]:


print result


# In[129]:


type(result)


# In[130]:


result = np.array(result)


# In[132]:


type(result)


# In[133]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')

plt.plot(result)
plt.show()


# In[135]:


import seaborn as sns 
import pandas as pd

df = pd.DataFrame(result)
plt.plot(result)
#plt.show()


# In[136]:


print result


# In[143]:


type (result)


# In[139]:


import seaborn as sns 
import pandas as pd

df  = pd.DataFrame(result)
plt.plot(df)
#plt.show()




# In[144]:


print result


# In[145]:


type (result )


# In[147]:


shape(result)


# In[148]:


print result


# In[149]:


type(result)


# In[150]:


result = np.squeeze(result)
print result


# In[152]:


type (result)


# In[154]:


print df


# In[155]:


type (result)


# In[157]:


result = result.tolist()


# In[158]:


type (result)


# In[159]:


result = list (result)


# In[161]:


type (result)


# In[162]:


result


# In[164]:


result [0]


# In[ ]:




