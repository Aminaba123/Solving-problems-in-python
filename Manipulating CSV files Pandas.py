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
 
df = pd.read_csv('C:\\Users\\bbartling\\Documents\\Python\\WB             
Data\\WB_RTU6data.csv', index_col='Date', parse_dates=True)    ======type( )===  pandas.core.frame.DataFrame      

#################################################################################################                 
data=data.T.to_dict().values()                 
                 
#################################################################################################                 
 
# this code read dates from a csv file and then separate and save dates in diffrent CSV files
src_path = "/home/vivek/Desktop/Work/stack/"
main_file = "/home/vivek/Desktop/Work/stack/main.csv"
import csv
import collections
import pprint

with open(main_file, "rb") as fp:
    root = csv.reader(fp, delimiter=',')
    result = collections.defaultdict(list)
    for row in root:
        year = row[0].split("-")[0]
        result[year].append(row)

print "Result:-"        
pprint.pprint(result)

for i,j in result.items():
    file_path = "%s%s.csv"%(src_path, i)
    with open(file_path, 'wb') as fp:
        writer = csv.writer(fp, delimiter=',')
        writer.writerows(j)

                 
#################################################################################################                 
import datetime

for row in LocalDate: 
    date = datetime.datetime.strptime (row,"%m/%d/%Y") 
    if date < datetime.datetime.strptime ( "01/08/2018", "%m/%d/%Y"):
        print row , date
    
#################################################################################################                
                 
string_date = "2013-09-28 20:30:55.78200"
abc = datetime.datetime.now()

if abc  > string_date :
    print True                
                 
#################################################################################################                 
                 
import csv
with open('crop_data.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print(', '.join(row))                 
                 
                 
#Indiana,Corn,Genetically, engineered, (GE), corn,Stacked, gene, varieties,2012,Percent, of, all, corn, planted,60
#Indiana,Corn,Genetically, engineered, (GE), corn,Stacked, gene, varieties,2013,Percent, of, all, corn, planted,73
#Indiana,Corn,Genetically, engineered, (GE), corn,Stacked, gene, varieties,2014,Percent, of, all, corn, planted,78
#Indiana,Corn,Genetically, engineered, (GE), corn,Stacked, gene, varieties,2015,Percent, of, all, corn, planted,76
#Indiana,Corn,Genetically, engineered, (GE), corn,Stacked, gene, varieties,2016,Percent, of, all, corn, planted,75
#Indiana,Corn,Genetically, engineered, (GE), corn,All, GE, varieties,2000,Percent, of, all, corn, planted,11
#Indiana,Corn,Genetically, engineered, (GE), corn,All, GE, varieties,2001,Percent, of, all, corn, planted,12
#Indiana,Corn,Genetically, engineered, (GE), corn,All, GE, varieties,2002,Percent, of, all, corn, planted,13
#Indiana,Corn,Genetically, engineered, (GE), corn,All, GE, varieties,2003,Percent, of, all, corn, planted,16
#Indiana,Corn,Genetically, engineered, (GE), corn,All, GE, varieties,2004,Percent, of, all, corn, planted,21
#Indiana,Corn,Genetically, engineered, (GE), corn,All, GE, varieties,2005,Percent, of, all, corn, planted,26
#Indiana,Corn,Genetically, engineered, (GE), corn,All, GE, varieties,2006,Percent, of, all, corn, planted,40
#Indiana,Corn,Genetically, engineered, (GE), corn,All, GE, varieties,2007,Percent, of, all, corn, planted,59
#Indiana,Corn,Genetically, engineered, (GE), corn,All, GE, varieties,2008,Percent, of, all, corn, planted,78
#Indiana,Corn,Genetically, engineered, (GE), corn,All, GE, varieties,2009,Percent, of, all, corn, planted,79
#Indiana,Corn,Genetically, engineered, (GE), corn,All, GE, varieties,2010,Percent, of, all, corn, planted,83
#Indiana,Corn,Genetically, engineered, (GE), corn,All, GE, varieties,2011,Percent, of, all, corn, planted,85
#Indiana,Corn,Genetically, engineered, (GE), corn,All, GE, varieties,2012,Percent, of, all, corn, planted,84
#Indiana,Corn,Genetically, engineered, (GE), corn,All, GE, varieties,2013,Percent, of, all, corn, planted,85
#Indiana,Corn,Genetically, engineered, (GE), corn,All, GE, varieties,2014,Percent, of, all, corn, planted,88
#Indiana,Corn,Genetically, engineered, (GE), corn,All, GE, varieties,2015,Percent, of, all, corn, planted,88
#Indiana,Corn,Genetically, engineered, (GE), corn,All, GE, varieties,2016,Percent, of, all, corn, planted,86                
                 
import csv
with open('crop_data.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        print row                 
                 
                 
#['Indiana,Corn,Genetically', 'engineered', '(GE)', 'corn,Stacked', 'gene', 'varieties,2012,Percent', 'of', 'all', 'corn', 'planted,60']
#['Indiana,Corn,Genetically', 'engineered', '(GE)', 'corn,Stacked', 'gene', 'varieties,2013,Percent', 'of', 'all', 'corn', 'planted,73']
#['Indiana,Corn,Genetically', 'engineered', '(GE)', 'corn,Stacked', 'gene', 'varieties,2014,Percent', 'of', 'all', 'corn', 'planted,78']
#['Indiana,Corn,Genetically', 'engineered', '(GE)', 'corn,Stacked', 'gene', 'varieties,2015,Percent', 'of', 'all', 'corn', 'planted,76']
#['Indiana,Corn,Genetically', 'engineered', '(GE)', 'corn,Stacked', 'gene', 'varieties,2016,Percent', 'of', 'all', 'corn', 'planted,75']
#['Indiana,Corn,Genetically', 'engineered', '(GE)', 'corn,All', 'GE', 'varieties,2000,Percent', 'of', 'all', 'corn', 'planted,11']
#['Indiana,Corn,Genetically', 'engineered', '(GE)', 'corn,All', 'GE', 'varieties,2001,Percent', 'of', 'all', 'corn', 'planted,12']
#['Indiana,Corn,Genetically', 'engineered', '(GE)', 'corn,All', 'GE', 'varieties,2002,Percent', 'of', 'all', 'corn', 'planted,13']
#['Indiana,Corn,Genetically', 'engineered', '(GE)', 'corn,All', 'GE', 'varieties,2003,Percent', 'of', 'all', 'corn', 'planted,16']
#['Indiana,Corn,Genetically', 'engineered', '(GE)', 'corn,All', 'GE', 'varieties,2004,Percent', 'of', 'all', 'corn', 'planted,21']
#['Indiana,Corn,Genetically', 'engineered', '(GE)', 'corn,All', 'GE', 'varieties,2005,Percent', 'of', 'all', 'corn', 'planted,26']
#['Indiana,Corn,Genetically', 'engineered', '(GE)', 'corn,All', 'GE', 'varieties,2006,Percent', 'of', 'all', 'corn', 'planted,40']
#['Indiana,Corn,Genetically', 'engineered', '(GE)', 'corn,All', 'GE', 'varieties,2007,Percent', 'of', 'all', 'corn', 'planted,59']
#['Indiana,Corn,Genetically', 'engineered', '(GE)', 'corn,All', 'GE', 'varieties,2008,Percent', 'of', 'all', 'corn', 'planted,78']
#['Indiana,Corn,Genetically', 'engineered', '(GE)', 'corn,All', 'GE', 'varieties,2009,Percent', 'of', 'all', 'corn', 'planted,79']
#['Indiana,Corn,Genetically', 'engineered', '(GE)', 'corn,All', 'GE', 'varieties,2010,Percent', 'of', 'all', 'corn', 'planted,83']
#['Indiana,Corn,Genetically', 'engineered', '(GE)', 'corn,All', 'GE', 'varieties,2011,Percent', 'of', 'all', 'corn', 'planted,85']
#['Indiana,Corn,Genetically', 'engineered', '(GE)', 'corn,All', 'GE', 'varieties,2012,Percent', 'of', 'all', 'corn', 'planted,84']
#['Indiana,Corn,Genetically', 'engineered', '(GE)', 'corn,All', 'GE', 'varieties,2013,Percent', 'of', 'all', 'corn', 'planted,85']
#['Indiana,Corn,Genetically', 'engineered', '(GE)', 'corn,All', 'GE', 'varieties,2014,Percent', 'of', 'all', 'corn', 'planted,88']
#['Indiana,Corn,Genetically', 'engineered', '(GE)', 'corn,All', 'GE', 'varieties,2015,Percent', 'of', 'all', 'corn', 'planted,88']
#['Indiana,Corn,Genetically', 'engineered', '(GE)', 'corn,All', 'GE', 'varieties,2016,Percent', 'of', 'all', 'corn', 'planted,86']                 

Hints:                 
# The csv module’s reader and writer objects read and write sequences.
# Programmers can also read and write data in dictionary form using the 'DictReader' and 'DictWriter' classes.                 

#####################################################################################################################
                 
def convertLines(lines):
    head = lines[0]
    del lines[0]
    infoDict = {}
    for line in lines: #Going through everything but the first line
        infoDict[line.split(",")[0]] = [tuple(line.split(",")[1:])]
    return infoDict

def read_file(filename):
    thefile = open(filename, "r")
    lines = []
    for i in thefile:
        lines.append(i)
    thefile.close()
    return lines

mydict = convertLines(read_file(filename))
print(mydict)                 
                 
#####################################################################################################################
                 
import csv
from collections import defaultdict

d_dict = defaultdict(list)
with open('file.txt') as f:
    reader = csv.reader(f)
    reader.next()
    for i in list(reader):
        d_dict[i[0]].append(tuple(i[1:]))

print dict(d_dict)                
                 
#####################################################################################################################                 

import csv
reader = csv.reader(open('CamCloseM6 4V300E10.csv'))

result = {}
for column in reader:
    key = column[0]
    if key in result:
        pass
    result[key] = column[1:]
print result
                 
#####################################################################################################################                 
                 
import csv
reader = csv.reader(open('CamCloseM6 4V300E10.csv'))

result = {row[0]:row[1:] for row in reader if row and row[0]}
print result                 
                 
                 
 #####################################################################################
                
 import csv
reader = csv.reader(open('test.csv'))

result = {row[0]:[i for i in row[1:] if i] for row in reader if row and row[0]}
print result                
                 
#####################################################################################                
                 
import csv
from collections import OrderedDict
result = OrderedDict()
with open('CamCloseM6 4V300E10.csv') as f:
    for row  in f:
        row=row.strip().split()
        key = row[0]
        result[key] = row[1:]
print result               
                 
#####################################################################################                

import csv
from collections import OrderedDict
result = OrderedDict()
with open('crop_data.csv') as f:
    for row  in f:
        row=row.strip().split()
        print row                 
                 
#####################################################################################                

# You can use a defaultdict to store the values and then print them out:
                 
import csv

from collections import defaultdict

with open(filename, 'r') as handle:
    reader = csv.DictReader(handle, ['name', 'miles', 'country'])
    data = defaultdict(list)

    for line in reader:
        data[line['name']).append(int(line['miles']))

    for runner, distances in data.items():
        print '{} ran a total of {} miles and an average of {} miles'.format(
            runner, sum(distances), sum(distances) / float(len(distances))
        )                
                 
#####################################################################################                 
import csv

from collections import defaultdict

filename = 'new-1.csv'

with open(filename, 'r') as handle:
    reader = csv.DictReader(handle)
    for line in reader:
        print line                 
                 
#####################################################################################               

import csv

from collections import defaultdict

with open(filename, 'r') as handle:
    reader = csv.DictReader(handle, ['name', 'miles', 'country'])
    data = defaultdict(list)

    for line in reader:
        data[line['name']).append(int(line['miles']))

    for runner, distances in data.items():
        print '{} ran a total of {} miles and an average of {} miles'.format(
            runner, sum(distances), sum(distances) / float(len(distances))
        )
             
#####################################################################################
# This returns list of ...             
varieties = []
with open('new-1.csv', 'r') as infile:
    for line in infile:
        #if "All GE varieties" in line:
        varieties.append(line.split(','))            
             
             
 #####################################################################################            
  # This returns list of ... but it contains string 
             
varieties = []
with open('new-1.csv', 'r') as infile:
    for line in infile:
        #if "All GE varieties" in line:
        varieties.append(line)           
           
             
#####################################################################################            
import csv

with open('employee_birthday.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
                  
#####################################################################################                  
# Read CSV with dictionary                   
import csv

with open('employee_birthday.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')                  
                  
#####################################################################################
                  
 with open('CamCloseM6 4V300E10.csv') as csv_file:
    header = [h.strip() for h in csv_file.next().split(',')]
    reader = csv.DictReader(csv_file, fieldnames=header)                 
                  
#####################################################################################                 
                  
import csv

# open the file in universal line ending mode 
with open('test.csv', 'rU') as infile:
  # read the file as a dictionary for each row ({header : value})
  reader = csv.DictReader(infile)
  data = {}
  for row in reader:
    for header, value in row.items():
      try:
        data[header].append(value)
      except KeyError:
        data[header] = [value]

# extract the variables you want
names = data['name']
latitude = data['latitude']
longitude = data['longitude']                  
                  
#####################################################################################                  
                  
def addDateColumn():
"""Adds time to the daily rainfall data. Reads the csv as chunks of 100k 
   rows at a time and outputs them, appending as needed, to a single csv. 
   Uses the column of the raster names to get the date.
"""
    df = pd.read_csv(pathlist[1]+"CHIRPS_tanz.csv", iterator=True, 
                     chunksize=100000) #read csv file as 100k chunks

    '''Do some stuff'''

    count = 1 #for indexing item in time list 
    for chunk in df: #for each 100k rows
        newtime = [] #empty list to append repeating times for different rows
        toiterate = chunk[chunk.columns[2]] #ID of raster nums to base time
        while count <= toiterate.max():
            for i in toiterate: 
                if i ==count:
                    newtime.append(newyears[count])
            count+=1
        print "Finished", str(chunknum), "chunks"
        chunk["time"] = newtime #create new column in dataframe based on time
        outname = "CHIRPS_tanz_time2.csv"
        #append each output to same csv, using no header
        chunk.to_csv(pathlist[2]+outname, mode='a', header=None, index=None)             
             
 #####################################################################################            
# Example CSV file data:             
             
# 1/2/2014,5,8,red
# 1/3/2014,5,2,green
# 1/4/2014,9,1,blue            
             
# Next, let's cover the reading of CSV files into memory:

import csv

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
        print(row[0])
        print(row[0],row[1],row[2],)             
             
 # Next, we will show how to pull out specific data from the spreadsheet and save it to a list variable:

 import csv

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)           
             
# Once we have this data, what can we do with it? Maybe we are curious about what color something was on a specific date.

import csv

with open('example.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    dates = []
    colors = []
    for row in readCSV:
        color = row[3]
        date = row[0]

        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)

    # now, remember our lists?

    whatColor = input('What color do you wish to know the date of?:')
    coldex = colors.index(whatColor)
    theDate = dates[coldex]
    print('The date of',whatColor,'is:',theDate)
              
##################################################################################
df = pd.read_csv('estimated_pred.csv')

for i in range(1,100):
    df['X_t'+str(i)] = df['X'].shift(i)

###############################################################              

dic = {"John": "john@example.com", "Mary": "mary@example.com"} #dictionary

download_dir = "exampleCsv.csv" #where you want the file to be downloaded to 

csv = open(download_dir, "w") 
#"w" indicates that you're writing strings to the file

columnTitleRow = "name, email\n"
csv.write(columnTitleRow)

for key in dic.keys():
	name = key
	email = dic[key]
	row = name + "," + email + "\n"
	csv.write(row)              
              
              
 ###############################################################             
              
from pandas import parser

try:
  df=pd.read_csv('mydata.tsv',sep='\t',header=0, skiprows=[1,2,3])
except (parser.CParserError) as detail:
  print  detail
	      
 ###############################################################             

	      df=pd.read_csv('my_data.tsv',sep='\t',header=0, skiprows=[1,2,3])
###############################################################
	      
import csv
file = 'your_filename.csv' # use your filename
lines_set = set([100, 200]) # use your bad lines numbers here

with open(file) as f_obj:
    for line_number, row in enumerate(csv.reader(f_obj)):
        if line_number > max(lines_set):
            break
        elif line_number in lines_set: # put your bad lines numbers here
            print(line_number, row)	      
	      
###############################################################
	      
import csv


def read_my_lines(file, lines_list, reader=csv.reader):
    lines_set = set(lines_list)
    with open(file) as f_obj:
        for line_number, row in enumerate(csv.reader(f_obj)):
            if line_number > max(lines_set):
                break
            elif line_number in lines_set:
                print(line_number, row)


if __name__ == '__main__':
    read_my_lines(file='your_filename.csv', lines_list=[100, 200])	      
	      
	      
	      
###############################################################	      
	      
	      
bad_lines = []
with open(filename, 'r') as f:
    n_col = len(f.readline().split(';'))
    for i, line in enumerate(f):
        if len(line.split(';')) != n_col:
            print(i+2, line)
            bad_lines.append(i+2)
print(bad_lines)	      
	      
###############################################################	      
	      
