
# Current directory 

pwd 

# change directory 

cd C:...

######################################################################    
# changing directory    
import os

os.chdir("C:\\Users\\abbasnam\\Downloads\\Files")    
    
######################################################################

# Current directory 

import os

for root, dirs, files in os.walk("."):  
    for filename in files:
        print(filename)
        
######################################################################

import os
arr = os.listdir('.')


import os
cwd = os.getcwd()
print cwd

######################################################################

import os
print os.getcwd()

######################################################################
o/p:"C :\Users\admin\myfolder"

1.To get the current directory folder name alone

import os
str1=os.getcwd()
str2=str1.split('\\')
n=len(str2)
print str2[n-1]

######################################################################

for i in os.listdir('C:\Users'):
    print i
    
######################################################################    

import os
os.listdir("C:") # returns list

######################################################################   

import os
start_path = '.' # current directory
for path,dirs,files in os.walk(start_path):
    for filename in files:
        print os.path.join(path,filename)
        
 ###################################################################### 

os.listdir('C:\Users')

###################################################################### 
  
[x for x in os.walk('.')]
  
######################################################################
# Find tex files in directory  
import os
items = os.listdir(".")

newlist = []
for names in items:
    if names.endswith(".txt"):
        newlist.append(names)
print newlist  
  
######################################################################  

pwd # gives current directory

cd ... # will change the directory

import os
os.listdir('C:')  # gives all files in this drive

import os
os.listdir('.')  # gives all files in this directory

######################################################################
def num_suffix(n):
    '''
    Returns the suffix for any given int
    '''
    suf = ('th','st', 'nd', 'rd')
    n = abs(n) # wise guy
    tens = int(str(n)[-2:])
    units = n % 10
    if tens > 10 and tens < 20:
        return suf[0] # teens with 'th'
    elif units <= 3:
        return suf[units]
    else:
        return suf[0] # 'th'  
  
  
######################################################################

import glob, os
os.chdir(".")
for file in glob.glob("*.csv"):
    print(file)
# crop_data.csv
######################################################################

import glob
glob.glob('./*.csv')

# ['.\\crop_data.csv']
######################################################################





















