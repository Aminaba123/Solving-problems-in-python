
# Current directory 

pwd 

# change directory 

cd C:...

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
  
  
  
  
  
  
  
  








