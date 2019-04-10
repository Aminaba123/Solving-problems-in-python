
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

def set_directory():
    print ('Enter the directory to be set: ')
    data = input()
    chdir(data + ':\\')
    print ('Enter name for the folder: ')
    data = input()
    create_directory(data)
    return True

######################################################################

import os

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

######################################################################

from os.path import join, getsize
for root, dirs, files in os.walk('C:'):
    print(root, "consumes")

######################################################################
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
root = 'C:\\Users\\An47880'

for path, subdirs, files in os.walk(root):
    for name in files:
        print os.path.join(path, name)

######################################################################

import glob
glob.glob('./*py')

######################################################################
# Find all files in a directory with extension .txt in Python

import glob, os
os.chdir("/mydir")
for file in glob.glob("*.txt"):
    print(file)
    
import os
for file in os.listdir("/mydir"):
    if file.endswith(".txt"):
        print(os.path.join("/mydir", file))    

######################################################################

import os
>>> path = '/usr/share/cups/charmaps'
>>> text_files = [f for f in os.listdir(path) if f.endswith('.txt')]
>>> text_files

######################################################################

import os
import sys
walk_dir = sys.argv[-1]
print walk_dir

#Make sure you understand the three return values of os.walk:

#for root, subdirs, files in os.walk(rootdir):
#has the following meaning:

#root: Current path which is "walked through"
#subdirs: Files in root of type directory
#files: Files in root (not in subdirs) of type other than directory
#And please use os.path.join instead of concatenating with a slash!
#Your problem is filePath = rootdir + '/' + file - you must concatenate the currently "walked" folder instead of the topmost folder.
#So that must be filePath = os.path.join(root, file). BTW "file" is a builtin, so you don't normally use it as variable name.

#Another problem are your loops, which should be like this, for example:

import os
import sys

walk_dir = sys.argv[1]

print('walk_dir = ' + walk_dir)

# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# be an absolute path as well. Example:
# walk_dir = os.path.abspath(walk_dir)
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))

for root, subdirs, files in os.walk(walk_dir):
    print('--\nroot = ' + root)
    list_file_path = os.path.join(root, 'my-directory-list.txt')
    print('list_file_path = ' + list_file_path)

    with open(list_file_path, 'wb') as list_file:
        for subdir in subdirs:
            print('\t- subdirectory ' + subdir)

        for filename in files:
            file_path = os.path.join(root, filename)

            print('\t- file %s (full path: %s)' % (filename, file_path))

            with open(file_path, 'rb') as f:
                f_content = f.read()
                list_file.write(('The file %s contains:\n' % filename).encode('utf-8'))
                list_file.write(f_content)
                list_file.write(b'\n')


######################################################################

import os

path = "/usr/tmp"

# Check current working directory.
retval = os.getcwd()
print "Current working directory %s" % retval

# Now change the directory
os.chdir( path )

# Check current working directory.
retval = os.getcwd()

print "Directory changed successfully %s" % retval

######################################################################







