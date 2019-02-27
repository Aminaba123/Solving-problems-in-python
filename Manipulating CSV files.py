# Divide date as day,month and year

# Your delimiter should be a comma instead of a semicolon if it's a CSV.
# You are splitting on a date string instead of a delimiter when you call a.split(x[i]). 
# You probably want to split on a ., since that's what's separating the date fields.
# Without changing too much code, the following code works for me. 
# It wasn't clear from your question what you want to actually do with the data, but I tried to demonstrate how you would get it.

import csv

with open('p2.csv') as csvfile:
    reader = csv.DictReader(
        csvfile, fieldnames=('date', 'stations', 'pcp'), delimiter=',', quotechar='|')
    next(reader)  # skip header row
    x = [row['date'] for row in reader]

for date_str in x:
    day, month, year = date_str.split('.')
    print(day, month, year)

#################################################################################################    
import numpy as np
from sklearn import preprocessing, cross_validation, neighbors, utils
import pandas as pd

df = pd.read_csv('C:\\Users\\bbartling\\Documents\\Python\\WB             
Data\\WB_RTU6data.csv', index_col='Date', parse_dates=True)

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())


X = np.array(df.drop(['VAV6znt'],1))
df.dropna(inplace=True)

y = np.array(df['VAV6znt'])


accuracies = []

X_train, X_test, y_train, y_test =             
cross_validation.train_test_split(X,y,test_size=0.50)

clf = neighbors.KNeighborsClassifier(n_neighbors=50)
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)

print(accuracy)
                 
#################################################################################################                 

for i in (range(len(data_csv_split)-9000)):
      print i

#################################################################################################
                 
                 
                 
                 
                 
